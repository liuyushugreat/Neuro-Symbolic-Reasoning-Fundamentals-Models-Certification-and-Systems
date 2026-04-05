# Appendix C — Course Labs and Practice Projects

The following labs pair with chapters in the main text and can be extended with the open repository [SkyNetUamPlatform](https://github.com/liuyushugreat/SkyNetUamPlatform).

## Lab 1: Small low-altitude ontology and rule encoding

Work with Chapters 5–6 to model domain objects and the SkyKG concept and rule layers.

**Code entry:** {doc}`experiments/lab1_ontology_rules.py <../experiments/lab1_ontology_rules>`

```python
"""
Lab 1 — code overview
====================
Goals:
1. Show a minimal runnable “domain knowledge modeling + rule encoding” pipeline.
2. Help readers turn Chapter 5 domain objects and Chapter 6 three-layer ontology / rule-layer ideas
   into executable Python data structures.

Structure:
1. EntityType / RelationType — concept-layer entity and relation types.
2. Rule / MinSeparationRule / NoFlyZoneRule — executable rules in the rule layer.
3. LowAltitudeOntology — unified entity types, relation types, facts, and rules.
4. build_demo_ontology() — construct a small low-altitude example.
5. print_summary() — print ontology, facts, and rule firings.

Core techniques:
1. Dataclasses for a lightweight ontology.
2. Store KG facts as relation → list of tuples.
3. Rules implement evaluate() for “match facts → raise alerts.”
4. Two representative rules: minimum separation; restricted / no-fly zone.

Concepts:
1. Domain taxonomy: Aircraft, Airspace, Mission, Facility, Operator
2. Relations: in_zone, distance_between, assigned_to, operated_by
3. Rule objects: separation constraints, restricted airspace
4. Knowledge substrate: concept, instance, and rule layers
5. Symbolic reasoning: explicit rule matching and alerting
"""

from dataclasses import dataclass, field
from typing import Dict, List, Tuple


@dataclass
class EntityType:
    name: str
    attributes: List[str]


@dataclass
class RelationType:
    name: str
    subject_type: str
    object_type: str


@dataclass
class Rule:
    name: str
    description: str

    def evaluate(self, facts: Dict[str, List[Tuple]]) -> List[str]:
        raise NotImplementedError


@dataclass
class MinSeparationRule(Rule):
    min_distance: float

    def evaluate(self, facts: Dict[str, List[Tuple]]) -> List[str]:
        alerts = []
        for uav_a, uav_b, distance in facts.get("distance_between", []):
            if distance < self.min_distance:
                alerts.append(
                    f"[{self.name}] Separation between {uav_a} and {uav_b} is {distance:.1f} m, "
                    f"below minimum safe distance {self.min_distance:.1f} m"
                )
        return alerts


@dataclass
class NoFlyZoneRule(Rule):
    def evaluate(self, facts: Dict[str, List[Tuple]]) -> List[str]:
        alerts = []
        zones = {uav: zone for uav, zone in facts.get("in_zone", [])}
        restricted = {zone for zone, zone_type in facts.get("zone_type", []) if zone_type == "restricted"}
        for uav, zone in zones.items():
            if zone in restricted:
                alerts.append(f"[{self.name}] {uav} entered restricted airspace {zone}")
        return alerts


@dataclass
class LowAltitudeOntology:
    entity_types: Dict[str, EntityType] = field(default_factory=dict)
    relation_types: Dict[str, RelationType] = field(default_factory=dict)
    facts: Dict[str, List[Tuple]] = field(default_factory=dict)
    rules: List[Rule] = field(default_factory=list)

    def add_entity_type(self, name: str, attributes: List[str]) -> None:
        self.entity_types[name] = EntityType(name=name, attributes=attributes)

    def add_relation_type(self, name: str, subject_type: str, object_type: str) -> None:
        self.relation_types[name] = RelationType(name=name, subject_type=subject_type, object_type=object_type)

    def add_fact(self, relation: str, fact: Tuple) -> None:
        self.facts.setdefault(relation, []).append(fact)

    def run_rules(self) -> List[str]:
        messages = []
        for rule in self.rules:
            messages.extend(rule.evaluate(self.facts))
        return messages


def build_demo_ontology() -> LowAltitudeOntology:
    ontology = LowAltitudeOntology()

    # Five domain object types (Chapter 5-style)
    ontology.add_entity_type("Aircraft", ["id", "speed", "altitude", "status"])
    ontology.add_entity_type("Airspace", ["zone_id", "zone_type"])
    ontology.add_entity_type("Mission", ["mission_id", "priority"])
    ontology.add_entity_type("Facility", ["facility_id", "kind"])
    ontology.add_entity_type("Operator", ["operator_id", "name"])

    # Relation types
    ontology.add_relation_type("in_zone", "Aircraft", "Airspace")
    ontology.add_relation_type("distance_between", "Aircraft", "Aircraft")
    ontology.add_relation_type("assigned_to", "Aircraft", "Mission")
    ontology.add_relation_type("operated_by", "Aircraft", "Operator")

    # Facts
    ontology.add_fact("in_zone", ("UAV-01", "ZONE-R1"))
    ontology.add_fact("in_zone", ("UAV-02", "ZONE-N1"))
    ontology.add_fact("zone_type", ("ZONE-R1", "restricted"))
    ontology.add_fact("zone_type", ("ZONE-N1", "normal"))
    ontology.add_fact("distance_between", ("UAV-01", "UAV-02", 78.0))
    ontology.add_fact("assigned_to", ("UAV-01", "MISSION-EMERGENCY"))
    ontology.add_fact("operated_by", ("UAV-01", "OP-ALPHA"))

    # Rules
    ontology.rules.append(
        MinSeparationRule(
            name="Minimum separation rule",
            description="Distance between any two aircraft must be at least 100 m",
            min_distance=100.0,
        )
    )
    ontology.rules.append(
        NoFlyZoneRule(
            name="No-fly zone rule",
            description="Aircraft must not enter restricted airspace",
        )
    )
    return ontology


def print_summary(ontology: LowAltitudeOntology) -> None:
    print("=== Ontology summary ===")
    print("Entity types:")
    for entity in ontology.entity_types.values():
        print(f"- {entity.name}: {', '.join(entity.attributes)}")

    print("\nRelation types:")
    for relation in ontology.relation_types.values():
        print(f"- {relation.name}: {relation.subject_type} -> {relation.object_type}")

    print("\nFacts:")
    for relation, relation_facts in ontology.facts.items():
        for fact in relation_facts:
            print(f"- {relation}{fact}")

    print("\nRule firings:")
    for alert in ontology.run_rules():
        print(f"- {alert}")


if __name__ == "__main__":
    demo = build_demo_ontology()
    print_summary(demo)

```

## Lab 2: Static risk reasoning with KG + SPARQL-style queries + LLM-ready explanations

Work with Chapters 8–10 for SPARQL-style evidence extraction and constrained semantic generation.

**Code entry:** {doc}`experiments/lab2_static_risk_reasoning.py <../experiments/lab2_static_risk_reasoning>`

```python
"""
Lab 2 — code overview
====================
Goals:
1. Demonstrate “KG + SPARQL-style evidence extraction + rule checks + constrained explanation generation”
   for static risk reasoning.
2. Give a minimal engineering reading of the hybrid architecture in Chapters 8–10 and “grounded answers.”

Structure:
1. KnowledgeGraph — triple store for a minimal KG.
2. query() — basic graph retrieval.
3. mini_sparql_select() — toy SPARQL-like pattern matching.
4. rule_check() — explicit rule checks.
5. constrained_explanation() — build an “evidence + rules + conclusion” chain.
6. build_demo_graph() — sample facts for static risk reasoning.

Core techniques:
1. Triple storage: (subject, predicate, object).
2. Graph queries via exact pattern filters.
3. Rule reasoning from airspace type, mission type, battery state.
4. Explanations as structured “evidence → rule findings → final decision.”

Concepts:
1. Knowledge graphs and triples
2. SPARQL-style queries and evidence extraction
3. Rule objects and explicit constraints
4. Static risk reasoning
5. Explanation chains and traceable outputs
6. Grounded answering
"""

from dataclasses import dataclass
from typing import Iterable, List, Optional, Tuple


Triple = Tuple[str, str, str]


@dataclass
class KnowledgeGraph:
    triples: List[Triple]

    def query(
        self,
        subject: Optional[str] = None,
        predicate: Optional[str] = None,
        obj: Optional[str] = None,
    ) -> List[Triple]:
        return [
            triple
            for triple in self.triples
            if (subject is None or triple[0] == subject)
            and (predicate is None or triple[1] == predicate)
            and (obj is None or triple[2] == obj)
        ]


def mini_sparql_select(graph: KnowledgeGraph, patterns: Iterable[Tuple[Optional[str], Optional[str], Optional[str]]]) -> List[Triple]:
    result: List[Triple] = []
    for subject, predicate, obj in patterns:
        result.extend(graph.query(subject, predicate, obj))
    return result


def rule_check(graph: KnowledgeGraph, uav_id: str) -> List[str]:
    findings = []

    current_zone = graph.query(uav_id, "in_zone", None)
    if current_zone:
        zone = current_zone[0][2]
        zone_type = graph.query(zone, "zone_type", None)
        if zone_type and zone_type[0][2] == "weather_alert":
            findings.append(f"{uav_id} is currently in weather-risk airspace {zone}")

    mission = graph.query(uav_id, "mission_type", None)
    if mission and mission[0][2] == "medical":
        findings.append(f"{uav_id} is on a medical mission; elevate priority")

    if graph.query(uav_id, "battery_status", "low"):
        findings.append(f"{uav_id} has low battery; avoid entering high-risk corridors")

    return findings


def constrained_explanation(uav_id: str, evidence: List[Triple], findings: List[str]) -> str:
    evidence_lines = [f"- Evidence: {s} --{p}--> {o}" for s, p, o in evidence]
    rule_lines = [f"- Rule finding: {x}" for x in findings]

    if not findings:
        decision = "No high-risk rules fired; mission may continue."
    else:
        decision = "Risk rules fired; recommend human review or route adjustment."

    return "\n".join(
        [
            f"Subject: {uav_id}",
            "Explanation chain:",
            *evidence_lines,
            *rule_lines,
            f"- Final conclusion: {decision}",
        ]
    )


def build_demo_graph() -> KnowledgeGraph:
    return KnowledgeGraph(
        triples=[
            ("UAV-17", "in_zone", "ZONE-WEATHER-2"),
            ("ZONE-WEATHER-2", "zone_type", "weather_alert"),
            ("UAV-17", "mission_type", "medical"),
            ("UAV-17", "battery_status", "low"),
            ("UAV-17", "assigned_corridor", "CORRIDOR-A3"),
            ("CORRIDOR-A3", "capacity_status", "busy"),
        ]
    )


if __name__ == "__main__":
    graph = build_demo_graph()
    target_uav = "UAV-17"

    evidence = mini_sparql_select(
        graph,
        [
            (target_uav, None, None),
            (None, "zone_type", None),
            (None, "capacity_status", None),
        ],
    )
    findings = rule_check(graph, target_uav)

    print("=== Static risk reasoning ===")
    print(constrained_explanation(target_uav, evidence, findings))

```

## Lab 3: Conflict detection on temporal knowledge-graph snapshots

Work with Chapters 11–12 to train/evaluate a conflict-detection module on TKG snapshots.

**Code entry:** {doc}`experiments/lab3_tkg_conflict_detection.py <../experiments/lab3_tkg_conflict_detection>`

```python
"""
Lab 3 — code overview
====================
Goals:
1. Without a deep-learning framework, show “temporal KG snapshot → feature extraction → conflict detection”
   training and evaluation.
2. Connect to Chapter 11–12 ideas: temporal graph reasoning, dynamic risk scoring, conflict models.

Structure:
1. PairSample — dynamic relation sample for a UAV pair at a time.
2. generate_sample() — synthetic data generator.
3. features() — distance, relative speed, altitude gap.
4. train_logistic_regression() — toy logistic regression.
5. evaluate() — accuracy, precision, recall.
6. demo_tkg_snapshot() — online-style scoring on snapshots.

Core techniques:
1. Logistic regression as a stand-in for heavier GNN/TKG models (emphasizes statistical risk scoring).
2. Map distance / speed / altitude gap to conflict probability.
3. Gradient descent on binary cross-entropy–style loss.
4. Test-set metrics and online inference on new snapshots.

Concepts:
1. Temporal KG snapshots
2. Dynamic relational modeling
3. Risk feature engineering
4. Conflict detection models
5. Logistic regression and gradient descent
6. Dynamic risk scoring and online inference
"""

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

## Lab 4: Conformal prediction for risk outputs with confidence sets

Work with Chapter 15 to build prediction sets/intervals and interpret coverage.

**Code entry:** {doc}`experiments/lab4_conformal_prediction.py <../experiments/lab4_conformal_prediction>`

```python
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

```

## Lab 5: Cloud–edge collaborative reasoning prototype

Work with Chapters 18–20 to partition device–edge–cloud roles and event-driven flows.

**Code entry:** {doc}`experiments/lab5_edge_cloud_pipeline.py <../experiments/lab5_edge_cloud_pipeline>`

```python
"""
Lab 5 — code overview
====================
Goals:
1. Show a minimal “device–edge–cloud” layered reasoning prototype.
2. Map Chapters 18–20 ideas — compute/latency gap, tiered deployment, cloud–edge collaboration,
   event-driven flow — to an executable pipeline.

Structure:
1. Event — message object.
2. EdgeNode — lightweight checks on telemetry.
3. CloudNode — aggregate edge outputs and emit policies.
4. main() — telemetry stream → edge → cloud.

Core techniques:
1. Edge: light logic (separation threshold, summaries).
2. Cloud: higher-level policy (high-risk alerts, speed advisories).
3. Event-driven flow: telemetry → edge_alert / edge_summary → cloud decision.

Concepts:
1. Compute gap and tiered deployment
2. Cloud–edge collaboration
3. Event-driven scheduling
4. Closed-loop timely response
5. Risk alerts and policy downlink
6. Light rule reasoning vs. centralized decisions
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Event:
    event_type: str
    payload: Dict[str, object]


class EdgeNode:
    def __init__(self, node_id: str):
        self.node_id = node_id

    def process(self, event: Event) -> List[Event]:
        forwarded: List[Event] = []
        if event.event_type != "telemetry":
            return forwarded

        altitude = float(event.payload["altitude"])
        speed = float(event.payload["speed"])
        distance = float(event.payload["nearest_distance"])
        uav_id = str(event.payload["uav_id"])

        if distance < 100:
            forwarded.append(
                Event(
                    "edge_alert",
                    {
                        "uav_id": uav_id,
                        "level": "high",
                        "reason": f"nearest_distance={distance}",
                        "source": self.node_id,
                    },
                )
            )

        forwarded.append(
            Event(
                "edge_summary",
                {
                    "uav_id": uav_id,
                    "altitude": altitude,
                    "speed": speed,
                    "nearest_distance": distance,
                    "source": self.node_id,
                },
            )
        )
        return forwarded


class CloudNode:
    def process(self, events: List[Event]) -> List[str]:
        decisions = []
        for event in events:
            if event.event_type == "edge_alert":
                decisions.append(
                    f"[Cloud policy] {event.payload['uav_id']}: high-risk alert — execute conservative avoidance immediately"
                )
            elif event.event_type == "edge_summary":
                if float(event.payload["speed"]) > 22:
                    decisions.append(
                        f"[Cloud policy] {event.payload['uav_id']}: speed high — reduce cruise speed and await new route assignment"
                    )
        return decisions


def main() -> None:
    telemetry_stream = [
        Event("telemetry", {"uav_id": "UAV-01", "altitude": 120, "speed": 24, "nearest_distance": 82}),
        Event("telemetry", {"uav_id": "UAV-02", "altitude": 135, "speed": 16, "nearest_distance": 210}),
    ]

    edge = EdgeNode("edge-node-beijing-01")
    cloud = CloudNode()

    print("=== Cloud–edge reasoning prototype ===")
    forwarded_events: List[Event] = []
    for event in telemetry_stream:
        print(f"[Edge ingest] {event.payload}")
        results = edge.process(event)
        forwarded_events.extend(results)
        for result in results:
            print(f"[Edge emit] {result.event_type}: {result.payload}")

    print("\n=== Cloud aggregation ===")
    for decision in cloud.process(forwarded_events):
        print(decision)


if __name__ == "__main__":
    main()

```

## Lab 6: Joint agent with LLM-style orchestration, KG, and solvers

Work with Chapter 22 to practice GraphRAG patterns, tool calls, and rule-bounded agent loops.

**Code entry:** {doc}`experiments/lab6_ns_agent.py <../experiments/lab6_ns_agent>`

```python
"""
Lab 6 — code overview
====================
Goals:
1. Minimal prototype of “LLM-style agent + KG + rule checks + action planning” in one loop.
2. Illustrate Chapter 22: GraphRAG-like retrieval, tool calls, and agent operation inside rule bounds.

Structure:
1. MiniKG — tiny KG with keyword search.
2. tool_query_kg() — retrieval tool.
3. tool_rule_check() — rule tool.
4. tool_plan_action() — planning tool.
5. agent_loop() — chain retrieve → rules → plan.

Core techniques:
1. Retrieve structured context from the KG.
2. Run symbolic checks for prohibitions / alerts.
3. Produce action recommendations from context + rule outcomes.
4. Print an explicit three-step chain for traceable “grounded” answers.

Concepts:
1. Neuro-symbolic agents
2. Knowledge-graph retrieval
3. Tool calling
4. Rule-bounded behavior
5. Action planning
6. Simplified GraphRAG / retrieval-augmented reasoning
"""

from dataclasses import dataclass
from typing import Dict, List, Tuple


Triple = Tuple[str, str, str]


@dataclass
class ToolResult:
    tool_name: str
    content: str


class MiniKG:
    def __init__(self, triples: List[Triple]):
        self.triples = triples

    def search(self, keyword: str) -> List[Triple]:
        return [triple for triple in self.triples if keyword in triple[0] or keyword in triple[1] or keyword in triple[2]]


def tool_query_kg(kg: MiniKG, keyword: str) -> ToolResult:
    matches = kg.search(keyword)
    lines = [f"{s} --{p}--> {o}" for s, p, o in matches]
    return ToolResult("query_kg", "\n".join(lines) if lines else "No matching knowledge found.")


def tool_rule_check(context: str) -> ToolResult:
    violations = []
    if "weather_alert" in context:
        violations.append("Rule fired: weather-alert airspace — reduce autonomous decision authority")
    if "restricted" in context:
        violations.append("Rule fired: routine inspection missions prohibited in restricted airspace")
    if not violations:
        violations.append("No high-priority prohibition rules fired; suggestions may proceed")
    return ToolResult("rule_check", "\n".join(violations))


def tool_plan_action(context: str) -> ToolResult:
    if "weather_alert" in context:
        plan = "Suggested action: replan route to avoid the weather-alert zone and request human confirmation."
    else:
        plan = "Suggested action: hold current route and continue monitoring risk."
    return ToolResult("plan_action", plan)


def agent_loop(question: str, kg: MiniKG) -> Dict[str, str]:
    keyword = "UAV-42" if "UAV-42" in question else "ZONE"
    kg_result = tool_query_kg(kg, keyword)
    rule_result = tool_rule_check(kg_result.content)
    plan_result = tool_plan_action(kg_result.content + "\n" + rule_result.content)

    final_answer = "\n".join(
        [
            f"Question: {question}",
            "Agent reasoning chain:",
            f"[1] Retrieval tool:\n{kg_result.content}",
            f"[2] Rule check:\n{rule_result.content}",
            f"[3] Action planning:\n{plan_result.content}",
        ]
    )
    return {
        "question": question,
        "answer": final_answer,
    }


if __name__ == "__main__":
    kg = MiniKG(
        [
            ("UAV-42", "in_zone", "ZONE-WX-9"),
            ("ZONE-WX-9", "zone_type", "weather_alert"),
            ("UAV-42", "mission_type", "inspection"),
            ("UAV-42", "battery_status", "normal"),
            ("ZONE-R2", "zone_type", "restricted"),
        ]
    )

    result = agent_loop(
        "Assess whether UAV-42 should continue its inspection mission now and provide recommendations.",
        kg,
    )
    print("=== Neuro-symbolic agent prototype ===")
    print(result["answer"])

```
