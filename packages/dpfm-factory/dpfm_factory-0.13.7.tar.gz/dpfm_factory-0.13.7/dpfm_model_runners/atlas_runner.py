import asyncio
import json
import logging
import os
import time

import httpx
import nest_asyncio
import numpy as np
from dotenv import load_dotenv

nest_asyncio.apply()

logger = logging.getLogger()

# Load environment variables from .env file
load_dotenv()
APIGEE_CLIENT_KEY = os.getenv("APIGEE_CLIENT_KEY")
APIGEE_CLIENT_SECRET = os.getenv("APIGEE_CLIENT_SECRET")
if APIGEE_CLIENT_KEY is None:
    raise EnvironmentError(
        "You must define APIGEE_CLIENT_KEY in your .env file!")
if APIGEE_CLIENT_SECRET is None:
    raise EnvironmentError(
        "You must define APIGEE_CLIENT_SECRET in your .env file!")
ATLAS_BASE_URL = 'https://staging.internal.mcc.api.mayo.edu/genai-digipath-atlas'
APIGEE_AUTH_URL = 'https://staging.internal.mcc.api.mayo.edu/oauth/token'
apigee_auth = None
last_auth_time = 0


def request_apigee_auth(apigee_key: str = "", apigee_secret: str = "",
                        url: str = APIGEE_AUTH_URL) -> dict:
    assert apigee_key != "" and apigee_secret != "", "apigee_key and apigee_secret required"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'grant_type': 'client_credentials',
        'client_id': apigee_key,
        'client_secret': apigee_secret
    }
    with httpx.Client() as client:
        response = client.post(url, headers=headers, data=data)
    json_response: dict = json.loads(response.text)
    assert "access_token" in json_response, f"failed to get access token: {response.text}"
    return json_response


def atlas_inference(apigee_access_token: str, data: bytes, input_img_size: int,
                    target_img_size: int = 224, read_timeout_sec: int = 180):
    url = f'{ATLAS_BASE_URL}?input_img_size={input_img_size}&target_img_size={target_img_size}'
    headers = {
        'Authorization': f'Bearer {apigee_access_token}',
        'Content-Type': 'application/octet-stream'
    }
    transport = httpx.HTTPTransport(retries=3)
    with httpx.Client(transport=transport) as client:
        response = client.post(url, headers=headers, content=data,
                               timeout=read_timeout_sec)
    # Improved explicit raise for HTTP errors
    response.raise_for_status()
    return response


def robust_atlas_inference(data: bytes, input_img_size: int,
                           target_img_size: int = 224,
                           read_timeout_sec: int = 180,
                           max_retries: int = 20):
    global apigee_auth, last_auth_time

    if apigee_auth is None or (time.time() - last_auth_time > 900):
        apigee_auth = request_apigee_auth(APIGEE_CLIENT_KEY,
                                          APIGEE_CLIENT_SECRET)
        last_auth_time = time.time()

    apigee_access_token = apigee_auth['access_token']

    retries = max_retries
    sleep = 2

    while retries > 0:
        try:
            response = atlas_inference(apigee_access_token, data,
                                       input_img_size, target_img_size,
                                       read_timeout_sec)
            return response.text, response.status_code
        except httpx.HTTPStatusError as e:
            retries -= 1
            logger.error(
                f"ATLAS HTTP status error {e.response.status_code}, retrying... {e}")
        except Exception as e:
            retries -= 1
            logger.error(f"ATLAS unexpected error, retrying... {e}")

        if retries == 0:
            logger.error(
                "Atlas HTTP API request failed (max retries exceeded).")
            return str(e), 500

        time.sleep(sleep)
        sleep = min(sleep * 2,
                    60)  # capped exponential backoff (max 60 seconds)


class AsyncApigeeClient:
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        self.client = httpx.AsyncClient(timeout=httpx.Timeout(10, read=180))
        self._token = None
        self._token_expiry = 0
        self._lock = asyncio.Lock()

    async def get_token(self):
        async with self._lock:
            now = time.time()
            if self._token is None or (self._token_expiry - now) < 60:
                headers = {'Content-Type': 'application/x-www-form-urlencoded'}
                data = {
                    'grant_type': 'client_credentials',
                    'client_id': self.key,
                    'client_secret': self.secret
                }
                response = await self.client.post(APIGEE_AUTH_URL,
                                                  headers=headers, data=data)
                response.raise_for_status()
                result = response.json()
                self._token = result["access_token"]
                self._token_expiry = now + int(result.get("expires_in", 3600))
        return self._token

    async def atlas_inference(self, data: bytes, input_img_size: int,
                              target_img_size: int = 224, retries: int = 5):
        sleep = 2
        for attempt in range(retries):
            try:
                token = await self.get_token()
                url = f'{ATLAS_BASE_URL}?input_img_size={input_img_size}&target_img_size={target_img_size}'
                headers = {'Authorization': f'Bearer {token}',
                           'Content-Type': 'application/octet-stream'}
                response = await self.client.post(url, headers=headers,
                                                  content=data)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                logger.error(
                    f"Atlas API HTTPStatusError (attempt {attempt + 1}/{retries}): {e}")
                if attempt == retries - 1:
                    raise
            except Exception as e:
                logger.error(
                    f"Atlas API unexpected error (attempt {attempt + 1}/{retries}): {e}")
                if attempt == retries - 1:
                    raise
            await asyncio.sleep(sleep)
            sleep = min(sleep * 2, 60)


class AtlasLoader:
    def __init__(self, model_name="mayo/ATLAS", image_size=224, use_async=True):
        self.image_size = image_size
        self.device = None
        self.use_async = use_async
        if self.use_async:
            self.apigee_client = AsyncApigeeClient(APIGEE_CLIENT_KEY,
                                                   APIGEE_CLIENT_SECRET)
        else:
            self.apigee_client = None
        self.model = None
        self.processor = None

    def get_processor_and_model(self):
        return self.processor, self.model

    def get_image_embedding(self, image, processor=None, model=None,
                            device=None):
        rgb_image = image.convert('RGB').resize(
            (self.image_size, self.image_size))
        rgb_array = np.array(rgb_image).transpose(2, 0, 1)
        rgb_image_bytes = rgb_array.tobytes()

        if self.use_async:
            async def _async_embedding():
                response_dict = await self.apigee_client.atlas_inference(
                    rgb_image_bytes,
                    input_img_size=self.image_size
                )
                return np.squeeze(response_dict['cls_token'])

            return asyncio.run(_async_embedding())
        else:
            response_text, status = robust_atlas_inference(
                data=rgb_image_bytes,
                input_img_size=self.image_size
            )
            if status != 200:
                raise RuntimeError(f"Sync inference failed: {response_text}")
            response_dict = json.loads(response_text)
            return np.squeeze(response_dict['cls_token'])
