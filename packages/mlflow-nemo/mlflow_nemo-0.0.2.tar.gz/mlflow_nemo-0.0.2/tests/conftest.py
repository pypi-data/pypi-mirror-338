from unittest import mock

import pandas as pd
import pytest


@pytest.fixture
def mlflow_experiment():
    with mock.patch("mlflow.search_runs") as mock_search_runs:
        mock_data = {
            "run_id": ["run_1", "run_2", "run_3"],
            "tags.mlflow.runName": ["model_a", "model_b", "model_a"],
        }
        mock_df = pd.DataFrame(mock_data)

        mock_search_runs.return_value = mock_df
        yield "123"
