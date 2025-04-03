import os
from typing import Optional

import click
from mlflow.cli import cli

from mlflow.nemo.search import find_run


@cli.group("nemo", cls=click.Group)
def nemo():
    """Nemo plugin for MLflow."""
    pass


@nemo.command()
@click.argument(
    "name",
    type=str,
    required=True,
)
@click.option(
    "--experiment-id",
    default=lambda: os.getenv("MLFLOW_EXPERIMENT_ID", None),
    show_default="MLFLOW_EXPERIMENT_ID (if set)",
    help="Experiment ID, taken from MLFLOW_EXPERIMENT_ID if not provided.",
)
def find(name: str, experiment_id: Optional[str]):
    """Find the run_id based on the run NAME."""
    if experiment_id is None:
        click.echo(
            "--experiment-id or MLFLOW_EXPERIMENT_ID is required .",
            err=True,
        )
        raise click.Abort()

    found_runs = find_run(run_name=name, experiment_id=experiment_id)
    for run in found_runs:
        click.echo(run)


if __name__ == "__main__":
    cli()
