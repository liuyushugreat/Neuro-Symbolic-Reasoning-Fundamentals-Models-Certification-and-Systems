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
