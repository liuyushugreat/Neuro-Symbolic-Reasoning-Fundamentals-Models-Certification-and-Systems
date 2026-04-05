# Appendix C — Experiment Code

This directory provides minimal, runnable Python examples for **Appendix C: Course Labs and Practice Projects**.

Design principles:

- Prefer the Python standard library only, to lower the setup barrier
- Each lab runs standalone
- Emphasize methodology and engineering skeletons—not big data or peak performance
- Easy to swap in real `SkyNetUamPlatform` components, graph stores, model services, and LLM APIs

Files:

- `lab1_ontology_rules.py` — Small low-altitude ontology and rule encoding
- `lab2_static_risk_reasoning.py` — Static risk reasoning with KG + SPARQL-style queries + constrained explanations
- `lab3_tkg_conflict_detection.py` — Simplified conflict-detection train/eval on temporal snapshot features
- `lab4_conformal_prediction.py` — Prediction sets and empirical coverage for risk outputs
- `lab5_edge_cloud_pipeline.py` — Cloud–edge collaboration and event-driven prototype
- `lab6_ns_agent.py` — Joint agent prototype: KG retrieval + tool calls + rule-bounded planning

How to run:

```bash
python lab1_ontology_rules.py
python lab2_static_risk_reasoning.py
python lab3_tkg_conflict_detection.py
python lab4_conformal_prediction.py
python lab5_edge_cloud_pipeline.py
python lab6_ns_agent.py
```

Suggested order:

1. Run `lab1` and `lab2` for the knowledge substrate and static reasoning
2. Run `lab3` and `lab4` for dynamic risk and trustworthy calibration
3. Run `lab5` and `lab6` for deployment patterns and agent loops
