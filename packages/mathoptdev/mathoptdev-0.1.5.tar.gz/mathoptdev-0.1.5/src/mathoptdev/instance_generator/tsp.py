import random
import pydantic
from typing import Optional
from pathlib import Path
from ..logger import logger
import math

class TSPInstanceSchema(pydantic.BaseModel):
    name: Optional[str] = None
    num_cities: int = 5
    coord_range: int = 100
    seed: int = 42
    folder: Path = Path("tsp")

def set_name(instance: TSPInstanceSchema):
    if instance.name is None:
        instance.name = f"tsp_{instance.num_cities}"
    return instance

def get_file_path(instance: TSPInstanceSchema):
    return instance.folder / f"{instance.name}.mps"

def generate_tsp_mps(instance: TSPInstanceSchema):
    instance = set_name(instance)
    
    random.seed(instance.seed)
    num_cities = instance.num_cities
    coord_range = instance.coord_range
    # Generate random coordinates for cities
    cities = [(random.uniform(0, coord_range), random.uniform(0, coord_range)) 
             for _ in range(num_cities)]
    
    # Calculate distances between cities
    distances = {}
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                x1, y1 = cities[i]
                x2, y2 = cities[j]
                distances[(i,j)] = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    # Create MPS file
    # make sure the folder exists
    folder = instance.folder
    folder.mkdir(parents=True, exist_ok=True)
    with open(get_file_path(instance), 'w') as f:
        # Write header
        f.write("NAME          TSP\n")
        f.write("ROWS\n")
        
        # Objective function
        f.write(" N  OBJ\n")
        
        # Flow conservation constraints
        for i in range(num_cities):
            f.write(f" E  OUT{i}\n")  # Outgoing
            f.write(f" E  IN{i}\n")   # Incoming
        
        # Write columns section
        f.write("COLUMNS\n")
        for i in range(num_cities):
            for j in range(num_cities):
                if i != j:
                    var_name = f"x_{i}_{j}"
                    # Objective coefficient
                    f.write(f"    {var_name}  OBJ  {distances[(i,j)]:.2f}\n")
                    # Flow conservation coefficients
                    f.write(f"    {var_name}  OUT{i}  1\n")
                    f.write(f"    {var_name}  IN{j}  1\n")
        
        # Write RHS section
        f.write("RHS\n")
        for i in range(num_cities):
            f.write(f"    RHS    OUT{i}  1\n")
            f.write(f"    RHS    IN{i}  1\n")
        
        # Write bounds section
        f.write("BOUNDS\n")
        for i in range(num_cities):
            for j in range(num_cities):
                if i != j:
                    f.write(f" BV BND1    x_{i}_{j}\n")
        
        # Write end of file
        f.write("ENDATA\n")
    logger.info(f"TSP instance {instance.name} generated at {get_file_path(instance)}")
    return cities, distances

