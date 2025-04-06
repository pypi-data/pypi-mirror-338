import mathoptdev as opt
from mathoptdev.types import CreateJobsRequest, InstanceStrategyPair

instance_data = opt.queries.get_instances()
strategy_data = opt.queries.get_strategies()

instance_list = instance_data['instances']
strategy_list = strategy_data['strategies']

instance_count = len(instance_list)
strategy_count = len(strategy_list)

print(f"Found {instance_count} instances and {strategy_count} strategies")

pairs: list[InstanceStrategyPair] = []
# Build all pairs of instances and strategies
for instance in instance_list:
    for strategy in strategy_list:
        instance_id = instance['id']
        strategy_id = strategy['id']
        pairs.append(InstanceStrategyPair(instance_id=instance_id, strategy_id=strategy_id))

print(f"Creating {len(pairs)} jobs")

request = CreateJobsRequest(instance_strategy_pairs=pairs)
response = opt.create_jobs(request)
opt.pretty_log(response)