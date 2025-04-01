from dataclasses import asdict
import numpy as np

from benchmark.measure import measure_accuracy


from ghostumap import GhostUMAP2


# def get_data(data_name: str):
#     dl = DataLoader(data_name)
#     X, y, legend, precomputed_knn = dl.get_data().values()

#     return X, y, legend, precomputed_knn


def eval_accuracy(
    X: np.ndarray,
    hprams: dict,
    benchmark_type: str,
    n_iter: int = 10,
    precomputed_knn: tuple = (None, None),
):
    gu = GhostUMAP2(precomputed_knn=precomputed_knn)
    O, G, alive_ghosts = gu.fit_transform(X, benchmark=benchmark_type, **hprams)

    unstable_ghosts = gu.get_unstable_ghosts(
        distance=hprams.get("distance", 0.1),
        sensitivity=hprams.get("sensitivity", 1),
    )

    result = asdict(gu.get_results())

    f1, precision, recall = measure_accuracy(
        y_true=unstable_ghosts, y_pred=alive_ghosts
    )

    result["original_embedding"] = O
    result["ghost_embedding"] = G
    result["alive_ghosts"] = alive_ghosts
    result["unstable_ghosts"] = unstable_ghosts
    result["f1"] = f1
    result["precision"] = precision
    result["recall"] = recall

    return result


def eval_acc_dropping(X: np.ndarray, hprams: dict, n_iter=10):
    return eval_accuracy(X, hprams, "accuracy_dropping", n_iter)


def eval_acc_halving(X: np.ndarray, hprams: dict, n_iter=10):
    return eval_accuracy(X, hprams, "accuracy_halving", n_iter)


def eval_time_dropping():
    pass


def eval_time_halving():
    pass
