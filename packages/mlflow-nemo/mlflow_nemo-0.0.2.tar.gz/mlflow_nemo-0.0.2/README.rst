mlflow-nemo
===========

.. image:: https://github.com/kqf/mlflow-nemo/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/kqf/mlflow-nemo/actions
   :alt: Tests

.. image:: https://img.shields.io/pypi/dm/mlflow-nemo.svg
   :target: https://pypi.org/project/mlflow-nemo/
   :alt: PyPI Downloads

An MLflow plugin providing the ``nemo`` CLI command.

Installation
------------
You can install ``mlflow-nemo`` using pip:

.. code-block:: bash

    pip install mlflow-nemo

Usage
-----

This plugin extends the MLflow CLI with a new ``nemo`` command group.

To list available ``nemo`` commands, run:

.. code-block:: bash

    mlflow nemo --help

``find`` Command
^^^^^^^^^^^^^^^^

The ``find`` command helps locate MLflow runs based on their names.

**Usage:**

.. code-block:: bash

    mlflow nemo find <name> [--experiment-id EXPERIMENT_ID]

**Arguments:**

- ``name`` (required): The name of the run to find.
- ``--experiment-id`` (optional): The MLflow Experiment ID. If not provided, it defaults to the ``MLFLOW_EXPERIMENT_ID`` environment variable.

**Example:**

Find a run named ``some-run`` in experiment ID ``123`` and take the latest one:

.. code-block:: bash

    mlflow nemo find some-run --experiment-id 123 | head -n 1

If no ``--experiment-id`` is provided, the command will check the environment variable ``MLFLOW_EXPERIMENT_ID``.
