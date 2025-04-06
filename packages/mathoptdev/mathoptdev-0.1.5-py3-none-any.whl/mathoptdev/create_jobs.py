from .send_request import send_request
from .types import CreateJobsRequest

def create_jobs(request: CreateJobsRequest) -> dict:
    pairs = request.instance_strategy_pairs
    body = {
        "action": "create_jobs",
        "instance_strategy_pairs": [
            {
                "instance_id": pair.instance_id,
                "strategy_id": pair.strategy_id
            }
            for pair in pairs
        ]
    }
    return send_request(body)

