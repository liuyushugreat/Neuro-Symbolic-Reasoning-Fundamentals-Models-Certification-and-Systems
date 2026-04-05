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
