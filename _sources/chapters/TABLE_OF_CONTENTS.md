# [*Neuro-Symbolic Reasoning: Fundamentals, Models, Certification, and Systems*](INTRODUCTION_EN.md)

## — Knowledge graph–driven neuro-symbolic reasoning and trustworthy governance in low-altitude traffic: theory and practice

## Scope of the book

**Core objective:** Using “knowledge graph–driven neuro-symbolic reasoning and trustworthy governance” as the main line, this book explains the full technical chain of neuro-symbolic AI—from foundational theory and key models through certification mechanisms to system deployment—and takes **urban low-altitude traffic / UAM** as the primary scenario to develop a unified methodology that is **interpretable, calibratable, deployable, and governable**.

This book includes theoretical material related to the open-source project https://github.com/liuyushugreat/SkyNetUamPlatform.

---

# [Introduction: From the two-peaks dilemma in AI to the third path of neuro-symbolic AI](chapters/Chapter_01_The_Evolution_Fracture_and_Reconstruction_of_AI.md)

## Core objectives

Clarify the historical tension between symbolic and connectionist AI; explain why neuro-symbolic AI has again become central in safety-critical complex systems; and introduce **trustworthy governance of low-altitude traffic** as the overarching problem of the book.

### [Chapter 1: The evolution, fracture, and reconstruction of AI](chapters/Chapter_01_The_Evolution_Fracture_and_Reconstruction_of_AI.md)

- 1.1 The rise and fall of symbolic AI: from expert systems to the knowledge-engineering bottleneck
- 1.2 The rise of connectionism: deep learning’s success and the black-box crisis
- 1.3 The two-peaks dilemma: the long-standing split between strong perception and weak reasoning
- 1.4 Lessons from cognitive science: complementary mechanisms of System 1 and System 2
- 1.5 The proposal of neuro-symbolic AI: why unify perception, knowledge, reasoning, and decision-making
- 1.6 Special requirements in safety-critical settings: explanation, certification, robustness, real time
- 1.7 Low-altitude traffic / UAM: a representative challenge for neuro-symbolic AI
- 1.8 Main line and technical closed loop of this book: knowledge base—reasoning models—trustworthy certification—system deployment

---

# [Part I: Foundations—logic, representation, and learning](chapters/Chapter_02_Symbolic_Logic_Rule_Systems_and_Automated_Reasoning.md)

## Core objectives

Equip readers from diverse backgrounds with foundations in logic, knowledge representation, deep learning, and graph learning, laying a shared base for later neuro-symbolic integration.

### [Chapter 2: Symbolic logic, rule systems, and automated reasoning](chapters/Chapter_02_Symbolic_Logic_Rule_Systems_and_Automated_Reasoning.md)

- 2.1 Propositional logic and first-order predicate logic
- 2.2 Rules, constraints, and reasoning chains
- 2.3 Forward chaining, backward chaining, and resolution
- 2.4 Description logic and ontology languages: foundations
- 2.5 Uncertain logic and fuzzy logic: an introduction
- 2.6 From formal logic to engineering rule systems

### [Chapter 3: Knowledge graphs and domain knowledge representation](chapters/Chapter_03_Knowledge_Graphs_and_Domain_Knowledge_Representation.md)

- 3.1 Basic concepts of knowledge graphs: entities, relations, attributes, events
- 3.2 RDF, OWL, SPARQL, and graph query languages
- 3.3 Ontology construction: concept layer, relation layer, constraint layer
- 3.4 Event graphs, scene graphs, and temporal knowledge graphs
- 3.5 From multi-source heterogeneous data to unified knowledge representation
- 3.6 Knowledge graph updating, alignment, and consistency maintenance
- 3.7 From general KGs to domain-specific KGs

### [Chapter 4: Deep learning, graph learning, and neural representation](chapters/Chapter_04_Deep_Learning_Graph_Learning_and_Neural_Representation.md)

- 4.1 Basic ideas of deep representation learning
- 4.2 Inductive biases of neural networks and function approximation
- 4.3 Graph neural networks: message passing, relational modeling, graph representation
- 4.4 Transformer and attention mechanisms
- 4.5 Temporal modeling and learning dynamical systems
- 4.6 Limits of deep learning: OOD behavior, hallucination, catastrophic forgetting, fragility
- 4.7 From deep models to constrained learning

---

# [Part II: A unified knowledge base—domain modeling for low-altitude traffic](chapters/Chapter_05_Domain_Knowledge_Modeling_for_Trustworthy_Governance_in_Low_Altitude_Traffic.md)

## Core objectives

Make explicit a pivotal chapter derived from the author’s dissertation work (Chapter 3): build the shared knowledge base for all subsequent models.

### [Chapter 5: Domain knowledge modeling for trustworthy governance in low-altitude traffic](chapters/Chapter_05_Domain_Knowledge_Modeling_for_Trustworthy_Governance_in_Low_Altitude_Traffic.md)

- 5.1 Object system for low-altitude traffic / UAM: aircraft, airspace, missions, infrastructure, stakeholders
- 5.2 Modeling risk objects: conflict, violation, failure, environmental disturbance
- 5.3 Modeling rule objects: regulations, operational constraints, priority rules, safety boundaries
- 5.4 Spatiotemporal objects: routes, corridors, windows, dynamic occupancy
- 5.5 Scene semantic templates: logistics, inspection, emergency, air taxi
- 5.6 Risk labels and design of explanation units
- 5.7 From business language to knowledge language: unified semantic abstraction

### [Chapter 6: Low-altitude traffic knowledge graph construction and unified representation](chapters/Chapter_06_Low_Altitude_Traffic_Knowledge_Graph_Construction_and_Unified_Representation.md)

- 6.1 Ontology layering: concept layer, instance layer, rule layer
- 6.2 Entity–relation patterns and attribute modeling
- 6.3 Unified expression of static knowledge, dynamic state, and certification objects
- 6.4 Encoding rule constraints: logical rules, soft constraints, conflict resolution
- 6.5 Graph construction pipeline: acquisition, cleaning, mapping, fusion, updating
- 6.6 Multi-source data ingestion: telemetry, maps, weather, policy, and operation logs
- 6.7 How the unified knowledge base supports subsequent models

### [Chapter 7: Taxonomy and technology roadmap for neuro-symbolic systems](chapters/Chapter_07_A_Taxonomy_and_Technical_Roadmap_of_Neuro_Symbolic_Systems.md)

- 7.1 Classical taxonomy: Henry Kautz’s neuro-symbolic spectrum
- 7.2 A three-layer integration taxonomy: symbolic-dominant / hybrid-pipeline / deeply fused
- 7.3 Layer 1: rule-dominant knowledge-augmented systems
- 7.4 Layer 2: hybrid pipelines with KG + retrieval augmentation + language models
- 7.5 Layer 3: deeply fused models running directly on KG / TKG
- 7.6 Comparing the three paths: interpretability, real time, scalability, certification readiness
- 7.7 Main technical line of the book and chapter mapping

---

# Part III: Static cognition—knowledge graph–driven interpretable risk reasoning

## Core objectives

Explain how to build static interpretable reasoning frameworks with KG + RAG + LLM in settings that are rule-heavy, knowledge-dense, and demand very high interpretability.

### [Chapter 8: Basic paradigms of knowledge injection and constrained learning](chapters/Chapter_08_Basic_Paradigms_of_Knowledge_Injection_and_Constrained_Learning.md)

- 8.1 Loss-function formulations of logical rules
- 8.2 Constrained optimization and posterior regularization
- 8.3 Co-training of rules and neural models
- 8.4 Physical and mechanistic constraint networks
- 8.5 From knowledge injection to interpretable reasoning

### [Chapter 9: Hybrid neuro-symbolic reasoning driven by knowledge graphs](chapters/Chapter_09_Knowledge_Graph_Driven_Hybrid_Neuro_Symbolic_Reasoning.md)

- 9.1 SPARQL queries and deterministic evidence extraction
- 9.2 Semantic completion by LLMs and chain-style explanation generation
- 9.3 Applicability and limits of RAG in rule-dense scenarios
- 9.4 GraphRAG: from document retrieval to graph retrieval
- 9.5 Coupling external solvers with language models
- 9.6 From “being able to answer” to “answering with evidence”

### [Chapter 10: Designing interpretable risk reasoning frameworks—from SkyKG to a general methodology](chapters/Chapter_10_Design_of_an_Explainable_Risk_Reasoning_Framework_From_SkyKG_to_a_General_Methodology.md)

- 10.1 Problem definition for static risk reasoning
- 10.2 Coordinated organization of ontology + rules + retrieval indexes
- 10.3 Dual-channel reasoning: rule-query channel and semantic generation channel
- 10.4 Risk label outputs and explanation-chain generation
- 10.5 Faithfulness evaluation: rule alignment, unsupported-claim rate, evidence coverage
- 10.6 Strengths and boundaries of static single-body scenarios
- 10.7 Why move from static cognition to dynamic coordination

---

# Part IV: Dynamic coordination—temporal knowledge graphs and multi-agent real-time reasoning

## Core objectives

Focus on high-density, strongly time-varying, multi-agent interaction; explain how temporal KGs and graph neural networks support real-time conflict detection and coordinated de-confliction.

### [Chapter 11: Temporal knowledge graphs and dynamic relational reasoning](chapters/Chapter_11_Temporal_Knowledge_Graphs_and_Dynamic_Relational_Reasoning.md)

- 11.1 From static KG to temporal KG
- 11.2 Representing time, events, and state transitions
- 11.3 Dynamic relations and time-varying edge weights
- 11.4 Temporal logic and continuous-time modeling
- 11.5 Event-driven reasoning and dynamic updates
- 11.6 Applicability of dynamic graphs in traffic and flight systems

### [Chapter 12: Graph-driven multi-agent conflict detection models](chapters/Chapter_12_Graph_Driven_Multi_Agent_Conflict_Detection_Models.md)

- 12.1 Formalizing multi-UAV dynamic coordination
- 12.2 Graph attention and relation-aware message passing
- 12.3 Temporal encoding and stale-edge discounting
- 12.4 Spatiotemporally coupled conflict prediction
- 12.5 Real-time metrics: latency, throughput, stability
- 12.6 Accuracy metrics: CDR, FAR, F1, and warning lead time
- 12.7 From prediction to intervention: dynamic risk scores and priority ranking

### [Chapter 13: Coordinated de-confliction and decision-making on temporal relational graphs](chapters/Chapter_13_Cooperative_Deconfliction_and_Decision_Making_Based_on_Temporal_Relational_Graphs.md)

- 13.1 Relationship between conflict detection and conflict resolution
- 13.2 Generating avoidance strategies from paths and graph structure
- 13.3 Role of reinforcement learning in graph-path reasoning
- 13.4 Constraint-based coordinated de-confliction
- 13.5 Local optimality vs. global safety envelopes
- 13.6 From SkyFlow to a general dynamic reasoning framework

---

# Part V: Trustworthy certification—calibratable, provable, auditable neuro-symbolic reasoning

## Core objectives

Move “trustworthy AI” from loose discussion toward **certification-grade trustworthy reasoning**—the most dissertation-distinctive part of the book.

### [Chapter 14: Trustworthiness issues in neuro-symbolic systems](chapters/Chapter_14_Trustworthiness_Issues_in_Neuro_Symbolic_Systems.md)

- 14.1 Why neuro-symbolic systems are still not inherently trustworthy
- 14.2 Interpretability ≠ certifiability
- 14.3 Black-box confidence and overconfidence
- 14.4 Distribution shift, concept drift, and scenario transfer
- 14.5 Special trustworthiness requirements in safety-critical systems
- 14.6 From empirical performance to formal assurance

### [Chapter 15: Conformal prediction and uncertainty calibration](chapters/Chapter_15_Conformal_Prediction_and_Uncertainty_Calibration.md)

- 15.1 Types of uncertainty: epistemic vs. aleatoric
- 15.2 Why probabilistic outputs are not the same as trustworthy confidence
- 15.3 Basic principles of conformal prediction
- 15.4 Conformal methods in classification, regression, and set prediction
- 15.5 Conformal calibration for graph and temporal models
- 15.6 Conformal scoring design for neuro-symbolic outputs
- 15.7 Risk prediction intervals and coverage guarantees

### [Chapter 16: Online monitoring, distribution shift, and statistical certification](chapters/Chapter_16_Online_Monitoring_Distribution_Drift_and_Statistical_Certification.md)

- 16.1 Failure modes in online inference
- 16.2 Martingale methods and sequential consistency monitoring
- 16.3 Concept drift and anomalous-distribution detection
- 16.4 Trust scoring for static explanation chains
- 16.5 Certification wrapping for dynamic conflict prediction
- 16.6 From “interpretable output” to “certification-grade output”
- 16.7 SkyCert: systematic design of a certification bridge

### [Chapter 17: Interpretability evaluation, audit chains, and regulatory interfaces](chapters/Chapter_17_Explainability_Evaluation_Audit_Trails_and_Regulatory_Interfaces.md)

- 17.1 Layers of interpretability: local, rule-based, causal
- 17.2 Evaluating faithfulness, sufficiency, and comprehensibility
- 17.3 Audit log design for neuro-symbolic systems
- 17.4 How human supervisors use explanations and certificates
- 17.5 Interface issues with aviation / autonomous-driving safety standards
- 17.6 From model trustworthiness to governance trustworthiness

---

# Part VI: System foundations—city-scale cloud–edge neuro-symbolic reasoning architecture

## Core objectives

Corresponding to SkyGrid: land all prior algorithms in city-scale systems engineering.

### [Chapter 18: Complexity of neuro-symbolic reasoning and the compute gap](chapters/Chapter_18_The_Complexity_of_Neuro_Symbolic_Reasoning_and_the_Computing_Gap.md)

- 18.1 Sources of complexity in symbolic, graph, and large-model reasoning
- 18.2 Latency constraints of real-time systems
- 18.3 Concurrency pressure in city-scale low-altitude traffic
- 18.4 From algorithmic optimality to deployable utility
- 18.5 Necessity of layered deployment of the reasoning stack

### [Chapter 19: Distributed reasoning systems under cloud–edge collaboration](chapters/Chapter_19_Distributed_Reasoning_Systems_under_Cloud_Edge_Collaboration.md)

- 19.1 Division of roles between edge and cloud reasoning
- 19.2 Distributed orchestration of rule checking, GNN inference, and LLM inference
- 19.3 Streaming data ingestion and event-driven scheduling
- 19.4 Knowledge sync, model sync, and state consistency
- 19.5 Real-time alerting chains and closed-loop response
- 19.6 From single-node feasibility to multi-node scale-out

### [Chapter 20: Spatiotemporal graph partitioning and high-concurrency reasoning engines](chapters/Chapter_20_Spatiotemporal_Graph_Partitioning_and_High_Concurrency_Reasoning_Engines.md)

- 20.1 Spatiotemporal graph partitioning
- 20.2 Subgraph cuts, boundary coordination, and cross-region conflict propagation
- 20.3 Parallelism mechanisms in graph reasoning engines
- 20.4 Load balancing for large-scale conflict detection
- 20.5 Throughput and fault tolerance for city-scale thousand-UAV scenarios
- 20.6 SkyGrid: from research prototype to engineering base

### [Chapter 21: Platform realization—from stacking models to governance closed loops](chapters/Chapter_21_Platformization_From_Model_Stacking_to_Governance_Closed_Loop.md)

- 21.1 Integrating knowledge base—reasoning models—certification—deployment architecture
- 21.2 Modular design for platforms
- 21.3 Unifying data flow, control flow, and evidence flow
- 21.4 Multi-role interfaces for regulators, operators, and executors
- 21.5 From research systems to industry application platforms
- 21.6 Open-source ecosystems and reproducible experiments

---

# Part VII: Frontiers—large models, agents, and AI for Science

## Core objectives

Keep the textbook forward-looking without leaving the main line—extensions beyond the core thread.

### [Chapter 22: Neuro-symbolic AI in the large language model era](chapters/Chapter_22_Neuro_Symbolic_AI_in_the_Era_of_Large_Language_Models.md)

- 22.1 LLMs as System 1: strengths, hallucination, structural limitations
- 22.2 Coupling language models with symbolic rules
- 22.3 GraphRAG and knowledge-augmented reasoning
- 22.4 LLMs calling external solvers and toolchains
- 22.5 Neuro-symbolic agents: perceive—retrieve—reason—act
- 22.6 Agent coordination for complex governance systems

### [Chapter 23: Safety-critical industry applications](chapters/Chapter_23_Applications_in_Safety_Critical_Industries.md)

- 23.1 Intelligent transportation and autonomous driving: scene-graph understanding
- 23.2 Urban low-altitude traffic: risk assessment and dynamic coordination
- 23.3 Interpretable reasoning stacks in medical diagnosis
- 23.4 Industrial control and fault diagnosis in complex systems
- 23.5 From “usable” to “deployable with confidence”: key differences

### [Chapter 24: Neuro-symbolic reasoning in AI for Science](chapters/Chapter_24_Neuro_Symbolic_Reasoning_for_AI_for_Science.md)

- 24.1 Molecular graphs, scientific knowledge, and interpretable discovery
- 24.2 Physical constraints and scientific mechanism learning
- 24.3 Knowledge-augmented simulation in complex systems
- 24.4 Prospects for neuro-symbolic methods in cross-disciplinary science
- 24.5 Feedback from industry applications to foundational theory

---

# Closing: Summary and future research roadmap

### [Chapter 25: The future of neuro-symbolic reasoning—from interpretability toward certification, governance, and deployment](chapters/Chapter_25_The_Future_of_Neuro_Symbolic_Reasoning_From_Explainability_to_Certifiability_Governability_and_Deployability.md)

- 25.1 Summary of the main line: knowledge base, reasoning, certification, systems
- 25.2 Current bottlenecks: data, standards, benchmarks, certification, compute
- 25.3 Future direction I: unified world models and neuro-symbolic agents
- 25.4 Future direction II: certification-grade trustworthy AI
- 25.5 Future direction III: real-time governance of city-scale complex systems
- 25.6 Future direction IV: from UAM to broader safety-critical systems

---

# Appendices and labs

## [Appendix A: Mathematical, logical, and graph-learning notation](appendices/Appendix_A_Mathematical_Logical_and_Graph_Learning_Notation.md)

- A.1 Logical symbols and common rule templates
- A.2 Notation for graph neural networks and temporal graph models
- A.3 Conformal prediction and statistical calibration notation
- A.4 System architecture and complexity-analysis notation

## [Appendix B: Common open-source libraries and engineering tools](appendices/Appendix_B_Open_Source_Libraries_and_Engineering_Tools.md)

- B.1 PyKEEN
- B.2 DeepProbLog
- B.3 Logic Tensor Networks (LTN)
- B.4 PyTorch Geometric (PyG)
- B.5 RDFLib / OWLReady2 / Neo4j / GraphDB
- B.6 LLM + KG integration toolchains
- B.7 Streaming inference and edge deployment frameworks

## [Appendix C: Course labs and practice projects](appendices/Appendix_C_Course_Labs_and_Practice_Projects.md)

- Lab 1: Small low-altitude-traffic ontology construction and rule encoding
- Lab 2: Static risk reasoning with KG + SPARQL + LLM
- Lab 3: Conflict detection models on temporal knowledge graphs
- Lab 4: Conformal prediction for risk outputs with confidence intervals
- Lab 5: Prototype cloud–edge collaborative reasoning system
- Lab 6: Joint agent development with large models + knowledge graph + solvers

---

*For the English introduction and reading guide, see [INTRODUCTION_EN.md](INTRODUCTION_EN.md).*
