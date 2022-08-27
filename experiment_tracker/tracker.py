import os
from datetime import datetime
from typing import Union, Any, Hashable

import numpy as np
import pandas as pd
from matplotlib.lines import Artist
from matplotlib.figure import Figure


class ExperimentTracker:
    def __init__(self, story_name: str, experiment_name: str) -> None:
        self._story_name = story_name
        self._experiment_name = experiment_name

        self._parameters = {}
        self._results = {}

        self._experiment_directory = os.path.join(
            "experiment_results",
            self._story_name,
            f"{datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}_{experiment_name}"
        )
        self._make_folders()

    def __getitem__(self, item: Hashable) -> Any:
        return self._parameters[item]

    def add_parameter(self, name: str, value: str) -> None:
        self._parameters[name] = value

    def add_result(
        self,
        name: str,
        value: Union[str, int, float, np.ndarray, pd.DataFrame, pd.Series, dict]
    ) -> None:
        if isinstance(value, int) or isinstance(value, str) or isinstance(value, float):
            self._results[name] = value

    def add_plot(self, plot: Union[Artist, Figure], file_name: str) -> None:
        plot.savefig(os.path.join(self._experiment_directory, file_name))

    def save(self) -> None:
        with open(
            os.path.join(self._experiment_directory, "parameters_and_results.txt"), 'w'
        ) as f:
            for parameter_name, parameter_value in self._parameters.items():
                f.write(f"{parameter_name} = {parameter_value}\n")

    def _make_folders(self) -> None:
        os.makedirs(os.path.join("experiment_results"), exist_ok=True)
        os.makedirs(os.path.join("experiment_results", self._story_name), exist_ok=True)
        os.makedirs(self._experiment_directory, exist_ok=True)
