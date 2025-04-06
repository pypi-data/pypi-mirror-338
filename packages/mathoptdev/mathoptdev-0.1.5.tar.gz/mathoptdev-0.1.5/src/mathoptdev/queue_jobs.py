from .send_request import send_request
from .types import QueueJobsRequest

def queue_jobs(request: QueueJobsRequest) -> dict:
    body = {
        "action": "queue_jobs",
        "job_ids": request.job_ids  
    }
    return send_request(body)