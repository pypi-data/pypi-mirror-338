import numpy as np


def measure_accuracy(y_true, y_pred):
    TP = np.sum(np.logical_and(y_true == 1, y_pred == 1))
    FP = np.sum(np.logical_and(y_true == 0, y_pred == 1))
    FN = np.sum(np.logical_and(y_true == 1, y_pred == 0))
    TN = np.sum(np.logical_and(y_true == 0, y_pred == 0))

    precision = TP / (TP + FP) if TP + FP > 0 else 0
    recall = TP / (TP + FN) if TP + FN > 0 else 0

    f1 = (
        2 * (precision * recall) / (precision + recall) if precision + recall > 0 else 0
    )

    return f1, precision, recall


__all__ = ["measure_accuracy"]
