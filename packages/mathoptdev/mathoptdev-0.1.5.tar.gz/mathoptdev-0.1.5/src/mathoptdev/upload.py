import requests
from pydantic import BaseModel, field_validator
from typing import Optional

from .logger import logger
from .send_request import send_request

class PresignedUrlRequest(BaseModel):
    id: str
    file_size: str
    name: Optional[str] = None
    action: str = "create_instance"

    @field_validator("file_size")
    def validate_file_size(cls, v):
        # value has to be less than 10MB
        if int(v) > 10 * 1024 * 1024:
            raise ValueError("File size must be less than 10MB")
        return v

class PresignedUrlResponse(BaseModel):
    url: Optional[str] = None
    fields: Optional[dict] = None
    skip_upload: bool = False

def get_presigned_url(request: PresignedUrlRequest) -> PresignedUrlResponse:
    body = request.model_dump() 
    response = send_request(body)
    return PresignedUrlResponse(**response)


def upload_to_s3(response: PresignedUrlResponse, data: bytes):
    if response.skip_upload:
        logger.info("Skipping upload")
        return
    
    logger.info("Uploading to S3...")
    
    # Use the complete key path for the file
    # Prepare the form data with all required fields
    files = {
        'file': (response.fields['key'], data, 'application/gzip')
    }
    
    # Make the POST request to upload the file
    response = requests.post(
        response.url,
        data=response.fields,
        files=files
    )
    
    if response.status_code == 204:
        logger.info("Upload successful")
    else:
        response.raise_for_status()
        logger.error(f"Upload failed with status code: {response.status_code}") 