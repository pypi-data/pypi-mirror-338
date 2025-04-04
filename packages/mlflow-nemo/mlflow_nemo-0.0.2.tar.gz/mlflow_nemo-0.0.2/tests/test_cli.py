import os
from unittest.mock import patch

from click.testing import CliRunner

from mlflow.nemo.cli import find


def test_find_without_experiment_id():
    runner = CliRunner()
    result = runner.invoke(find, ["test_run"])
    assert result.exit_code == 1


def test_find_with_experiment_id(mlflow_experiment):
    runner = CliRunner()
    result = runner.invoke(find, ["test_run", "--experiment-id", "1"])
    assert result.exit_code == 0


def test_find_with_env_experiment_id(mlflow_experiment):
    runner = CliRunner()
    with patch.dict(os.environ, {"MLFLOW_EXPERIMENT_ID": "2"}):
        result = runner.invoke(find, ["test_run"])
    assert result.exit_code == 0
