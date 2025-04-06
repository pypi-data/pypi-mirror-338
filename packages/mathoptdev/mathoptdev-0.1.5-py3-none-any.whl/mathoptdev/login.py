import click
import webbrowser
import getpass

from .config import FRONTEND_ENDPOINT
from .token import save_token, get_stored_token
from .logger import logger
from .send_request import send_request

def get_user():
    body = {
        "action": "get_user"
    }
    response = send_request(body)
    return response

def login():
    """Login to MathOpt CLI"""
    try:
        token = get_stored_token()
        if token:
            logger.info("Already logged in.")
            get_user()
            return
    except ValueError:
        pass
    
    auth_url = f"{FRONTEND_ENDPOINT}/dashboard/tokens"
    
    logger.info("Opening browser for authentication...")
    webbrowser.open(auth_url)
    
    # Simple polling mechanism to wait for token
    logger.info("Waiting for authentication...")
    token = getpass.getpass("Please paste the token from the browser (it won't print to the console): ")
    assert token, "Token is required"
    
    path = save_token(token)
    logger.info(f"Saved token to {path}")

    get_user()


