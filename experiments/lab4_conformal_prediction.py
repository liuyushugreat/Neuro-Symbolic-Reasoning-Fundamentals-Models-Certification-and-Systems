"""
Lab 4 — code overview
====================
Goals:
1. Show how to wrap risk-classifier outputs with a conformal prediction layer.
2. Turn Chapter 15 concepts — nonconformity scores, prediction sets, coverage — into code.

Structure:
1. quantile() — calibration threshold qhat from nonconformity scores.
2. build_prediction_set() — build a prediction set given qhat.
3. empirical_coverage() — empirical coverage on a test stream.
4. main — calibration set, test set, sets, and coverage printout.

Core techniques:
1. Nonconformity score = 1 − p(y|x) (probability of the true class in calibration).
2. Calibrate on held-out scores; take (1 − α) quantile as threshold.
3. For a new sample, keep all classes with (1 − p_c) ≤ qhat.
4. Report empirical coverage on tests.

Concepts:
1. Uncertainty calibration
2. Conformal prediction
3. Nonconformity scores
4. Prediction sets
5. Coverage guarantees vs. empirical coverage
6. Risk-level classification outputs
"""

import math
from typing import List, Sequence, Tuple


def quantile(scores: Sequence[float], alpha: float) -> float:
    ordered = sorted(scores)
    n = len(ordered)
    index = math.ceil((n + 1) * (1 - alpha)) - 1
    index = max(0, min(index, n - 1))
    return ordered[index]


def build_prediction_set(probabilities: Sequence[float], threshold: float) -> List[int]:
    # Nonconformity score = 1 - p(y|x) for the predicted-class probability used in calibration
    return [cls for cls, p in enumerate(probabilities) if (1 - p) <= threshold]


def empirical_coverage(prediction_sets: Sequence[List[int]], labels: Sequence[int]) -> float:
    covered = sum(int(label in prediction_set) for prediction_set, label in zip(prediction_sets, labels))
    return covered / len(labels)


if __name__ == "__main__":
    alpha = 0.1

    # Calibration set: (true label, model probability assigned to that true label)
    calibration_data: List[Tuple[int, float]] = [
        (0, 0.92),
        (1, 0.76),
        (2, 0.63),
        (1, 0.84),
        (0, 0.80),
        (2, 0.58),
        (1, 0.70),
        (0, 0.87),
        (2, 0.66),
        (1, 0.62),
    ]
    calibration_scores = [1 - prob for _, prob in calibration_data]
    qhat = quantile(calibration_scores, alpha)

    # Test set: three-class risk levels 0=low, 1=medium, 2=high
    test_probabilities = [
        [0.79, 0.18, 0.03],
        [0.20, 0.51, 0.29],
        [0.16, 0.24, 0.60],
        [0.35, 0.38, 0.27],
        [0.09, 0.41, 0.50],
    ]
    test_labels = [0, 1, 2, 1, 2]

    prediction_sets = [build_prediction_set(probs, qhat) for probs in test_probabilities]
    coverage = empirical_coverage(prediction_sets, test_labels)

    print("=== Conformal prediction demo ===")
    print(f"alpha = {alpha}")
    print(f"qhat  = {qhat:.3f}")
    print()
    for i, (probs, pred_set, label) in enumerate(zip(test_probabilities, prediction_sets, test_labels), start=1):
        print(
            f"sample_{i}: probs={probs}, prediction_set={pred_set}, "
            f"label={label}, covered={label in pred_set}"
        )
    print()
    print(f"Empirical coverage = {coverage:.3f}")
