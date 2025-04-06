# MathOpt

To interact with mathopt, we provide a CLI and a Python SDK. It contains tools to help developers solve combinatorial problems in the cloud. 

## Installation 

Install with pip
```bash
pip install mathoptdev
```
Install with uv (recommended package manager): 
```bash
uv add mathoptdev 
```
This installs a CLI that you can call with:
```bash
opt --help 
```
or 

```bash
alias opt="uv run opt" # set and alias for uv
opt --help 
```
## Login 

This command will guide you through the login process:
```bash
opt login 
```
We store the API token in the MATHOPT_API_TOKEN variable in your .env file. 

After logging in, check the user with 
```bash
opt user 
```

## REST API
You can call the API directly with a HTTP POST request. You need to specify the x-mathopt-api-token header. 

```bash
curl -X POST https://www.mathopt.dev/api \
  -H "x-mathopt-api-token: YOUR_MATHOPT_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "action": "get_user"
  }'
```
We also have a helper function in python

```python
import mathoptdev as opt 
body = {
  "action": "get_user"
}
opt.send_request(body) 
```

## Create problem instances 
To get you started, we provide the following helper command that generates a Travelling Salesman Problem (TSP):

```bash
opt tsp -c 5 
```
The option `-c` corresponds to the number of cities in the problem. The MPS file will be saved in the tsp folder in your current directory. 

Once instances are generated, upload them with the following command: 
```bash
opt instance create tsp 
```
To verify that we successfully processed your instances, you can query the backend with the command:
```bash
opt instance list 
```
or in python
```python
import mathoptdev as opt 
opt.queries.get_instances() 
```

## Solve instances 
To solve an instance, you need to create a job with its id and the id of the strategy you want to use to solve it. 

The list of available strategies can be queried with 
```bash
opt strategy list 
```

We provide an example on how to create and queue a set of jobs in these scripts: 
- [create_jobs.py](https://github.com/laroccacharly/mathoptdev/blob/main/examples/create_jobs.py)
- [queue_jobs.py](https://github.com/laroccacharly/mathoptdev/blob/main/examples/queue_jobs.py)

# Monitor your jobs
You can monitor your jobs with:
```bash
opt job list 
```
or 
```python
import mathoptdev as opt 
opt.queries.get_jobs() 
```

# Download solutions
You can download the parquet file associated with a solution:
```python
import mathoptdev as opt 
body = {
  "action": "download_solution",
  "solution_id": "my_solution_id"
}
opt.send_request(body) 
```
There is a full example at the link: 
[download_solutions.py](https://github.com/laroccacharly/mathoptdev/blob/main/examples/download_solution.py)
