from mlflow.nemo.search import find_run


def test_finds_run(mlflow_experiment):
    find_run(experiment_id=mlflow_experiment, run_name="test-run-1")
