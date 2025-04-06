# A collection is a set of instances
# We assume that some .mps or .mps.gz files are in the path COLLECTION_PATH
# We iterate over all the files, if the file is a .mps, we zip it. It is a .mps.gz, we do nothing.
# We combine all the .mpz.gz files into a single tar.gz file
# We send a request to the server to get a presigned url
# The server will return a url and a set of fields to send in the request body
# We send the .tar.gz file to the url 

import gzip
import tarfile
import io
from pathlib import Path
from typing import List
from pydantic import BaseModel

from .logger import logger
from .utils import human_readable_size, hash_for_bytes
from .upload import upload_to_s3, PresignedUrlResponse
from .send_request import send_request

def _compress_mps_file(mps_path: Path) -> Path:
    """Compress a .mps file if it's not already compressed."""
    compressed_path = mps_path.with_suffix('.mps.gz')
    if compressed_path.exists():
        logger.info(f"Compressed file already exists: {compressed_path}")
        return compressed_path
    
    logger.info(f"Compressing {mps_path}")
    raw_bytes = mps_path.read_bytes()
    compressed = gzip.compress(raw_bytes)
    compressed_path.write_bytes(compressed)
    logger.info(f"Compression ratio: {len(compressed)/len(raw_bytes):.2f}")
    return compressed_path

def _validate_collection_path(path: Path) -> None:
    """Validate that the collection path exists and contains at least one MPS file."""
    if not path.exists():
        raise ValueError(f"Path does not exist: {path}")
    if not path.is_dir():
        raise ValueError(f"Path is not a directory: {path}")
    
    mps_files = list(path.glob("*.mps"))
    mps_gz_files = list(path.glob("*.mps.gz"))
    
    if not mps_files and not mps_gz_files:
        raise ValueError(f"No .mps or .mps.gz files found in {path}")

def prepare_collection(collection_path: str, collection_name: str = None) -> tuple[bytes, str]:
    """Prepare a collection of .mps/.mps.gz files as a single tar.gz archive.
    
    Args:
        collection_path: String path to the directory containing .mps files (relative or absolute)
        collection_name: Optional name for the collection, defaults to directory name
    
    Returns:
        tuple containing (tar_bytes, collection_name)
    """
    # Convert string path to Path object and resolve to absolute path
    path = Path(collection_path).resolve()
    _validate_collection_path(path)
    
    if collection_name is None:
        collection_name = path.name

    logger.info(f"Processing collection: {collection_name} from {path}")
    
    # Check if tar.gz already exists
    tar_path = path / f"{collection_name}.tar.gz"
    if tar_path.exists():
        logger.info(f"Using existing archive: {tar_path}")
        tar_bytes = tar_path.read_bytes()
        logger.info(f"Collection size: {human_readable_size(len(tar_bytes))}")
        logger.info(f"Collection hash: {hash_for_bytes(tar_bytes)}")
        return tar_bytes, collection_name
    
    # Find all .mps and .mps.gz files
    mps_files = list(path.glob("*.mps"))
    mps_gz_files = list(path.glob("*.mps.gz"))
    
    # Compress any uncompressed .mps files
    compressed_files: List[Path] = mps_gz_files.copy()
    for mps_file in mps_files:
        compressed_files.append(_compress_mps_file(mps_file))
    
    # Create a tar.gz archive in memory
    tar_buffer = io.BytesIO()
    with tarfile.open(fileobj=tar_buffer, mode='w:gz') as tar:
        for file_path in compressed_files:
            tar.add(file_path, arcname=file_path.name)
    tar_bytes = tar_buffer.getvalue()
    
    # Save the tar.gz file
    tar_path.write_bytes(tar_bytes)
    logger.info(f"Saved archive to: {tar_path}")
    
    logger.info(f"Collection size: {human_readable_size(len(tar_bytes))}")
    logger.info(f"Collection hash: {hash_for_bytes(tar_bytes)}")
    return tar_bytes, collection_name


class UploadCollectionRequest(BaseModel):
    id: str
    file_size: str
    name: str
    action: str = "create_instance_collection"

def send_upload_request(request: UploadCollectionRequest) -> PresignedUrlResponse:
    body = request.model_dump()
    response = send_request(body)
    return PresignedUrlResponse(**response)

def create_collection(collection_path: str, collection_name: str = None):
    """Upload a collection of .mps/.mps.gz files as a single tar.gz archive.
    
    Args:
        collection_path: String path to the directory containing .mps files (relative or absolute)
        collection_name: Optional name for the collection, defaults to directory name
    """
    tar_bytes, collection_name = prepare_collection(collection_path, collection_name)
    collection_hash = hash_for_bytes(tar_bytes)
    
    # Get presigned URL for upload
    request = UploadCollectionRequest(
        file_size=str(len(tar_bytes)),
        id=collection_hash,
        name=collection_name
    )
    response = send_upload_request(request)
    upload_to_s3(response, tar_bytes)

