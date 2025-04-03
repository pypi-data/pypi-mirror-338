from typing import List

import mlflow


def find_run(experiment_id: str, run_name: str) -> List[str]:
    runs = mlflow.search_runs(experiment_ids=[experiment_id])

    matching_runs = runs[
        runs["tags.mlflow.runName"].str.contains(run_name, na=False)
    ]

    return matching_runs["run_id"].tolist()
