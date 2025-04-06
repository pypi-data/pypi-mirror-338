import requests 
from .config import get_api_endpoint
from .auth import get_auth_headers
from .send_request import handle_raise_for_status

def send_stream_request(body: dict) -> list:
    """Send a streaming request to the API and return collected responses"""
    response = requests.post(
        get_api_endpoint(),
        headers=get_auth_headers(),
        json=body,
        stream=True
    )
    handle_raise_for_status(response)
    
    collected_responses = []
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')  
            print(decoded_line)
            collected_responses.append(decoded_line)
    
    return collected_responses
