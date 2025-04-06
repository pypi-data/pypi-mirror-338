import pydantic 

class InstanceStrategyPair(pydantic.BaseModel):
    instance_id: str
    strategy_id: str

class CreateJobsRequest(pydantic.BaseModel):
    instance_strategy_pairs: list[InstanceStrategyPair]

class QueueJobsRequest(pydantic.BaseModel):
    job_ids: list[str]