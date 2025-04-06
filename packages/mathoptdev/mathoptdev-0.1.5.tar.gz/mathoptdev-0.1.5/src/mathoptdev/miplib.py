import gzip
from pathlib import Path

from .logger import logger
from .utils import human_readable_file_size, hash_for_bytes
from .upload import upload_to_s3, PresignedUrlRequest, PresignedUrlResponse, get_presigned_url

def upload_instance(instance_path: Path): 
    instance_name = instance_path.stem
    logger.info(f"Uploading instance: {instance_name}")
    logger.info(f"File size: {human_readable_file_size(instance_path)}")
    # Read file and generate hash first
    raw_bytes = instance_path.read_bytes()
    instance_hash = hash_for_bytes(raw_bytes)
    logger.info(f"Instance hash: {instance_hash}")
    
    # Check if compressed file exists, stem.mps.gz
    compressed_path = instance_path.with_suffix(".mps.gz")
    if compressed_path.exists():
        logger.info("Compressed file already exists")
        compressed_size = compressed_path.stat().st_size
        logger.info(f"Compressed file size: {human_readable_file_size(compressed_path)}")
        compressed = compressed_path.read_bytes()
    else:
        # Compress after generating hash from raw bytes
        logger.info("Compressing instance...")
        compressed = gzip.compress(raw_bytes)
        logger.info(f"Compressed ratio: {len(compressed)/len(raw_bytes):.2f}")
        logger.info(f"Writing compressed file to {compressed_path}")
        compressed_path.write_bytes(compressed)

    compressed_size = len(compressed)

    # Upload to S3
    request = PresignedUrlRequest(
        file_size=str(compressed_size),
        id=instance_hash,
        action="create_instance",
        name=instance_name
    )
    response: PresignedUrlResponse = get_presigned_url(request)
    if response.skip_upload:
        logger.info("Skipping upload")
        return
    upload_to_s3(response, compressed)


def try_upload_instance(instance_path: Path):
    try:
        upload_instance(instance_path)
    except Exception as e:
        logger.error(f"Failed to upload instance: {instance_path.stem}")
        logger.error(e)
        if hasattr(e, 'response'):  # For HTTP-related errors that might have a response
            logger.error(f"Response body: {e.response.text}")
    

