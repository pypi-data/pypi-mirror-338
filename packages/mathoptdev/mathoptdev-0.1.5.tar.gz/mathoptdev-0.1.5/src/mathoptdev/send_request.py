import requests 
from .config import get_api_endpoint
from .auth import get_auth_headers
from .logger import logger

def handle_raise_for_status(response: requests.Response):
    is_error = response.status_code >= 400
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred: {e}")
        logger.error(f"Response body: {e.response.text}")
    return is_error

def send_request(body: dict) -> dict:
    response = requests.post(
        get_api_endpoint(),
        headers=get_auth_headers(),
        json=body
    )
    is_error = handle_raise_for_status(response)
    if is_error:
        return dict()
    response_dict = response.json()
    assert type(response_dict) == dict
    return response_dict

