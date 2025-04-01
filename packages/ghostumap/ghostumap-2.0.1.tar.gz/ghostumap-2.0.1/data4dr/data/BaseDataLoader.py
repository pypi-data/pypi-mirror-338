import json
import os
from abc import ABC, abstractmethod

import numpy as np
from umap import UMAP

from .model import DataModel


def _validate_path(paths: dict):
    return all(os.path.exists(path) for path in paths.values())


def _load_npy_file(path):
    return np.load(path, mmap_mode=None) if os.path.exists(path) else None


def _load_json_file(path, key):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f).get(key)
    return None


class BaseDataLoader(ABC):
    def __init__(self):
        self.base_path = None
        self._data = None
        self._label = None
        self._legend = None
        self._precomputed_knn = None

    @abstractmethod
    def load_raw_data(self):
        raise FileNotFoundError("Data not found")

    def drop_cache(self, paths):
        for path in paths:
            if os.path.exists(path):
                os.remove(path)

    def _get_paths(self):
        return {
            "data": os.path.join(self.base_path, "data.npy"),
            "label": os.path.join(self.base_path, "label.npy"),
            "legend": os.path.join(self.base_path, "legend.json"),
            "knn_indices": os.path.join(self.base_path, "knn_indices.npy"),
            "knn_dists": os.path.join(self.base_path, "knn_dists.npy"),
        }

    def load_data(self, get_knn: bool = True, n_neighbors: int = 15):
        paths = self._get_paths()
        knn_paths = {k: paths[k] for k in ["knn_indices", "knn_dists"]}

        if not os.path.exists(paths["data"]):
            self.load_raw_data()

        self._data = _load_npy_file(paths["data"])
        self._label = _load_npy_file(paths["label"])
        self._legend = _load_json_file(paths["legend"], "legend")

        if get_knn and not _validate_path(knn_paths):
            self._precomputed_knn = self.compute_knn(self._data, n_neighbors)
            self.save_data(paths["knn_indices"], self._precomputed_knn[0])
            self.save_data(paths["knn_indices"], self._precomputed_knn[1])

        elif get_knn:
            self._precomputed_knn = (
                _load_npy_file(knn_paths["knn_indices"]),
                _load_npy_file(knn_paths["knn_dists"]),
            )
        else:
            self._precomputed_knn = (None, None)

    def save_data(self, file_path, data):
        if not os.path.exists(file_path):
            np.save(file_path, data)

    def get_data(self) -> DataModel:
        result = {
            "data": self._data,
            "label": self._label,
            "legend": self._legend,
            "precomputed_knn": self._precomputed_knn,
        }

        return result

    def scale_data(self, data: np.ndarray):
        from sklearn.preprocessing import StandardScaler

        scaler = StandardScaler()
        return scaler.fit_transform(data)

    def compute_knn(self, X, n_neighbors: int = 15):
        if X.shape[0] < 4096:
            self._precomputed_knn = (None, None)
            return self._precomputed_knn

        X = self.scale_data(X)
        reducer = UMAP(n_neighbors=n_neighbors)
        _ = reducer.fit_transform(X)
        self._precomputed_knn = (reducer._knn_indices, reducer._knn_dists)

        return self._precomputed_knn
