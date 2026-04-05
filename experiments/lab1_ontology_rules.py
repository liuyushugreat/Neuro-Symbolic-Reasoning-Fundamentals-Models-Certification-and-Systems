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
