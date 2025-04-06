from pathlib import Path
from .logger import logger
from .config import MATHOPT_API_TOKEN_NAME

def logout():
    """Removes the MathOpt API token from the .env file."""
    env_path = Path('.env')
    
    if not env_path.exists():
        logger.info("No .env file found. Already logged out.")
        return

    try:
        lines = env_path.read_text().splitlines()
        
        new_lines = [line for line in lines if not line.strip().startswith(f'{MATHOPT_API_TOKEN_NAME}=')]
        
        if len(new_lines) == len(lines):
            logger.info("Token not found in .env file. Already logged out.")
        else:
            new_content = '\n'.join(new_lines).strip()
            if new_content:
                env_path.write_text(new_content + '\n')
            else:
                # If the file becomes empty, delete it
                env_path.unlink() 
            logger.info(f"Successfully logged out. Token removed from {env_path}")

    except Exception as e:
        logger.error(f"Error during logout: {e}") 