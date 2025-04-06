import pathlib
import hashlib
import json
from .logger import logger

def human_readable_size(size_in_bytes: int) -> str:
    size = float(size_in_bytes)
    for unit in ['bytes', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} TB"

def human_readable_file_size(path: pathlib.Path) -> str:
    size = path.stat().st_size
    return human_readable_size(size)

def hash_for_bytes(file_bytes: bytes, length: int = 16) -> str:
    return hashlib.sha256(file_bytes).hexdigest()[:length]  

def pretty_log(data: dict):
    pretty_json = json.dumps(data, indent=4)
    logger.info(pretty_json)