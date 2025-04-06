import os
from pathlib import Path
from dotenv import load_dotenv
from .logger import logger
from .config import MATHOPT_API_TOKEN_NAME

def get_stored_token() -> str | None:
    # First check if token is in environment
    token = os.getenv(MATHOPT_API_TOKEN_NAME)
    if token:
        return token
        
    # If not found, try loading from .env file
    load_dotenv()
    token = os.getenv(MATHOPT_API_TOKEN_NAME)
    if token:
        return token    
    
    raise ValueError(f"API token not found. Please set the {MATHOPT_API_TOKEN_NAME} environment variable or run `opt login`.")


def save_token(token: str) -> Path:
    # Create .env file if it doesn't exist
    env_path = Path('.env')
    
    # Read existing contents if file exists
    existing_content = ''
    if env_path.exists():
        existing_content = env_path.read_text()
        
    # Update or append MATHOPT_TOKEN
    if f'{MATHOPT_API_TOKEN_NAME}=' in existing_content:
        lines = existing_content.splitlines()
        new_lines = [line if not line.startswith(f'{MATHOPT_API_TOKEN_NAME}=') else f'{MATHOPT_API_TOKEN_NAME}={token}'
                    for line in lines]
        new_content = '\n'.join(new_lines)
    else:
        new_content = f"{existing_content}\n{MATHOPT_API_TOKEN_NAME}={token}"
    
    # Write back to .env file
    env_path.write_text(new_content.strip() + '\n')
    logger.info(f"Token saved to {env_path}")
    return env_path
