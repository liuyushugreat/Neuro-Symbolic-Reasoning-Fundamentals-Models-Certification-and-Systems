# Lab 3: Temporal KG Conflict Detection

**Related chapters:** Ch. 11 (Temporal Knowledge Graphs) · Ch. 12 (Conflict Detection Models)

This lab shows "temporal KG snapshot → feature extraction → conflict detection" training and evaluation without a deep-learning framework, connecting to Chapter 11–12 ideas on temporal graph reasoning, dynamic risk scoring, and conflict models.

## Design

- **PairSample** — dynamic relation sample for a UAV pair at a time
- **generate_sample()** — synthetic data generator
- **features()** — distance, relative speed, altitude gap
- **train_logistic_regression()** — toy logistic regression via gradient descent
- **evaluate()** — accuracy, precision, recall
- **demo_tkg_snapshot()** — online-style scoring on snapshots

## Key concepts

1. Temporal KG snapshots
2. Dynamic relational modeling
3. Risk feature engineering
4. Conflict detection models
5. Logistic regression and gradient descent
6. Dynamic risk scoring and online inference

## How to run

```bash
python lab3_tkg_conflict_detection.py
```

## Source code

```python
import math
import random
from dataclasses import dataclass
from typing import List, Tuple


random.seed(7)


@dataclass
class PairSample:
    distance_m: float
    relative_speed: float
    altitude_gap: float
    label: int


def sigmoid(x: float) -> float:
    if x >= 0:
        z = math.exp(-x)
        return 1 / (1 + z)
    z = math.exp(x)
    return z / (1 + z)


def generate_sample() -> PairSample:
    distance = random.uniform(30, 500)
    relative_speed = random.uniform(0, 50)
    altitude_gap = random.uniform(0, 120)

    risk_score = 2.0
    risk_score += 0.06 * (120 - min(distance, 120))
    risk_score += 0.08 * relative_speed
    risk_score += 0.05 * (40 - min(altitude_gap, 40))
    probability = sigmoid((risk_score - 4.5) / 2.0)
    label = 1 if random.random() < probability else 0
    return PairSample(distance, relative_speed, altitude_gap, label)


def features(sample: PairSample) -> List[float]:
    return [
        1.0,
        sample.distance_m / 500.0,
        sample.relative_speed / 50.0,
        sample.altitude_gap / 120.0,
    ]


def predict(weights: List[float], x: List[float]) -> float:
    return sigmoid(sum(w * v for w, v in zip(weights, x)))


def train_logistic_regression(train_data: List[PairSample], epochs: int = 800, lr: float = 0.2) -> List[float]:
    weights = [0.0, -1.0, 1.0, -0.8]
    for _ in range(epochs):
        grads = [0.0 for _ in weights]
        for sample in train_data:
            x = features(sample)
            pred = predict(weights, x)
            err = pred - sample.label
            for i in range(len(weights)):
                grads[i] += err * x[i]
        for i in range(len(weights)):
            weights[i] -= lr * grads[i] / len(train_data)
    return weights


def evaluate(weights: List[float], test_data: List[PairSample]) -> Tuple[float, float, float]:
    tp = fp = tn = fn = 0
    for sample in test_data:
        pred = 1 if predict(weights, features(sample)) >= 0.5 else 0
        if pred == 1 and sample.label == 1:
            tp += 1
        elif pred == 1 and sample.label == 0:
            fp += 1
        elif pred == 0 and sample.label == 0:
            tn += 1
        else:
            fn += 1

    accuracy = (tp + tn) / max(1, len(test_data))
    precision = tp / max(1, tp + fp)
    recall = tp / max(1, tp + fn)
    return accuracy, precision, recall


def demo_tkg_snapshot(weights: List[float]) -> None:
    snapshots = [
        PairSample(distance_m=75, relative_speed=32, altitude_gap=18, label=1),
        PairSample(distance_m=180, relative_speed=10, altitude_gap=55, label=0),
        PairSample(distance_m=52, relative_speed=36, altitude_gap=10, label=1),
    ]
    print("\n=== TKG snapshot risk scores ===")
    for i, sample in enumerate(snapshots, start=1):
        score = predict(weights, features(sample))
        print(
            f"snapshot_{i}: distance={sample.distance_m:.1f}m, "
            f"relative_speed={sample.relative_speed:.1f}, altitude_gap={sample.altitude_gap:.1f}m, "
            f"conflict_prob={score:.3f}"
        )


if __name__ == "__main__":
    data = [generate_sample() for _ in range(260)]
    train_data = data[:200]
    test_data = data[200:]

    model = train_logistic_regression(train_data)
    accuracy, precision, recall = evaluate(model, test_data)

    print("=== Simplified conflict detection (train / eval) ===")
    print("Model weights:", [round(w, 4) for w in model])
    print(f"accuracy={accuracy:.3f}")
    print(f"precision={precision:.3f}")
    print(f"recall={recall:.3f}")

    demo_tkg_snapshot(model)
```
