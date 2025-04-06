import mathoptdev as opt

solution_data = opt.queries.get_solutions()
solutions = solution_data['solutions']
# sort by created_at (latest first)
solutions.sort(key=lambda x: x['created_at'], reverse=True)
first_solution = solutions[0]

solution_id = first_solution['id']
print(f"Getting download url for solution id {solution_id}")
body = {
    "action": "download_solution",
    "solution_id": solution_id
}

response = opt.send_request(body)
download_url = response['download_url']

import requests
from tqdm import tqdm

print(f"Downloading solution...")
response = requests.get(download_url, stream=True)
total_size = int(response.headers.get('content-length', 0))

# Download with progress bar
with open('solution.parquet', 'wb') as f:
    with tqdm(total=total_size, unit='iB', unit_scale=True) as pbar:
        for data in response.iter_content(chunk_size=1024):
            size = f.write(data)
            pbar.update(size)
print(f"Download completed!")

# Read the parquet file using pandas
import pandas as pd
df = pd.read_parquet('solution.parquet')

print(df)

    
    