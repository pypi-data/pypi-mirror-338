import click

from .login import login as login_command
from .logout import logout as logout_command
from .collection import create_collection as create_collection_command
from .send_request import send_request
from .instance_generator.tsp import TSPInstanceSchema, generate_tsp_mps
from . import queries as q
from .utils import pretty_log


@click.group()
def cli():
    pass

@cli.command()
def login():
    login_command()

@cli.command()
def logout():
    """Log out by removing the API token from the .env file."""
    logout_command()

@cli.command()
def user():
    data = q.get_user()
    pretty_log(data)

@cli.group()
def instance():
    pass

@instance.command()
def list():
    data = q.get_instances()
    pretty_log(data)

@instance.command()
@click.argument('path', type=click.Path(exists=True))
def create(path):
    create_collection_command(path)

@cli.group()
def strategy():
    pass

@strategy.command()
def list():
    data = q.get_strategies()
    pretty_log(data)

@cli.group()
def job():
    pass

@job.command()
def list():
    data = q.get_jobs()
    pretty_log(data)

@cli.group()
def solution():
    pass

@solution.command()
def list():
    data = q.get_solutions()
    pretty_log(data)

@cli.command()
@click.option('-c', '--num-cities', type=int, default=5, help='Number of cities in the TSP instance')
def tsp(num_cities): 
    instance = TSPInstanceSchema(num_cities=num_cities, coord_range=100, seed=42)
    generate_tsp_mps(instance)






