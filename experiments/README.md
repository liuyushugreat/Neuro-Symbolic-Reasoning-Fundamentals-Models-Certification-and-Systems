# Appendix C — Experiment Code

This directory provides minimal, runnable Python examples for **Appendix C: Course Labs and Practice Projects**.

Design principles:

- Prefer the Python standard library only, to lower the setup barrier
- Each lab runs standalone
- Emphasize methodology and engineering skeletons—not big data or peak performance
- Easy to swap in real `SkyNetUamPlatform` components, graph stores, model services, and LLM APIs

## Labs

| Lab | Topic | Related Chapters |
|-----|-------|-----------------|
| {doc}`Lab 1 <lab1_ontology_rules>` | Small low-altitude ontology and rule encoding | Ch. 5–6 |
| {doc}`Lab 2 <lab2_static_risk_reasoning>` | Static risk reasoning with KG + SPARQL-style queries | Ch. 8–10 |
| {doc}`Lab 3 <lab3_tkg_conflict_detection>` | Conflict-detection train/eval on temporal snapshot features | Ch. 11–12 |
| {doc}`Lab 4 <lab4_conformal_prediction>` | Prediction sets and empirical coverage for risk outputs | Ch. 15 |
| {doc}`Lab 5 <lab5_edge_cloud_pipeline>` | Cloud–edge collaboration and event-driven prototype | Ch. 18–20 |
| {doc}`Lab 6 <lab6_ns_agent>` | Neuro-symbolic agent: KG retrieval + tool calls + rule-bounded planning | Ch. 22 |

## How to run

```bash
python lab1_ontology_rules.py
python lab2_static_risk_reasoning.py
python lab3_tkg_conflict_detection.py
python lab4_conformal_prediction.py
python lab5_edge_cloud_pipeline.py
python lab6_ns_agent.py
```

## Suggested order

1. Run **Lab 1** and **Lab 2** for the knowledge substrate and static reasoning
2. Run **Lab 3** and **Lab 4** for dynamic risk and trustworthy calibration
3. Run **Lab 5** and **Lab 6** for deployment patterns and agent loops
