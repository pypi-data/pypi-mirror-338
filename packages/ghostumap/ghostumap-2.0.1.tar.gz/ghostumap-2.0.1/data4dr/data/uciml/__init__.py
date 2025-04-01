import os
import json
from typing import Literal

from data4dr.data import BaseDataLoader

import numpy as np
import pandas as pd

from umap import UMAP

TUciml = Literal["ionosphere", "optical_recognition", "raisin", "htru2"]

data_id = {
    "ionosphere": 52,
    "optical_recognition": 80,
    "raisin": 850,
    "htru2": 372,
}

legend_to_label = {
    "ionosphere": {
        "g": 0,
        "b": 1,
    },
    "optical_recognition": {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    },
    "raisin": {
        "Kecimen": 0,
        "Besni": 1,
    },
    "htru2": {
        "0": 0,
        "1": 1,
    },
}


class UcimlLoader(BaseDataLoader):
    def __init__(self, name: TUciml = "ionosphere"):
        super().__init__()
        self.name = name
        self.base_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), self.name
        )
        self.load_data()

    def load_raw_data(self):
        from ucimlrepo import fetch_ucirepo

        fetched_data = fetch_ucirepo(id=data_id[self.name])

        # data (as pandas dataframes)
        X = fetched_data.data.features.values
        y = fetched_data.data.targets.values.flatten()

        self._data = self.scale_data(X)
        self._label = np.array([legend_to_label[self.name][str(label)] for label in y])
        self._legend = list(legend_to_label[self.name].keys())

        self._precomputed_knn = self.compute_knn(self._data)

        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)

        self.paths = self._get_paths()

        self.save_data(self.paths["data"], self._data)
        self.save_data(self.paths["label"], self._label)

        if self._precomputed_knn[0] is not None:
            self.save_data(self.paths["knn_indices"], self._precomputed_knn[0])
            self.save_data(self.paths["knn_dists"], self._precomputed_knn[1])

        with open(self.paths["legend"], "w") as f:
            json.dump({"legend": self._legend}, f)
