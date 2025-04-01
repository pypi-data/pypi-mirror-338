import json
import os

from data4dr.data import BaseDataLoader

import numpy as np
import pandas as pd


class Cifar10Loader(BaseDataLoader):
    def __init__(self):
        super().__init__()
        self.name = "cifar10"
        self.base_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), self.name
        )
        self.load_data()

    def load_raw_data(self):
        self._data = np.load(os.path.join(self.base_path, "data.npy"))
        self._label = np.load(os.path.join(self.base_path, "label.npy"))
        self._legend = json.load(open(os.path.join(self.base_path, "legend.json"))).get(
            "legend"
        )

        self._precomputed_knn = self.compute_knn(self._data)

        self.save_precomputed_knn(self.base_path)
