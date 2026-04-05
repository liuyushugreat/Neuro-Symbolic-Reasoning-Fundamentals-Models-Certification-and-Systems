

This appendix lists curated open-source tools for neuro-symbolic algorithms, knowledge-graph construction, and cloud–edge deployment. For Appendix C labs or a low-altitude governance prototype, you can compose a toolchain from the sections below.

### B.1 PyKEEN
**PyKEEN (Python KnowledgE EmbeddiNgs)** is a leading Python library for training and evaluating knowledge-graph embedding (KGE) models.
* **Core capabilities:** Dozens of classic KGE models (TransE, RotatE, ComplEx, …) with standard training pipelines and metrics (MRR, Hits@K).
* **Use in this book:** Chapters 8–9 embed static SkyKG topology (e.g., airspace adjacency, route connectivity) into dense vectors as priors for downstream deep models.

### B.2 DeepProbLog
**DeepProbLog** is a prominent probabilistic logic programming framework for neuro-symbolic AI, extending ProbLog with neural components.
* **Core capabilities:** Neural networks appear as **neural predicates** in first-order rules; the engine performs exact logical inference and backpropagation over hybrid programs.
* **Use in this book:** Fits Layer 1/2 hybrid systems (Chapter 7). Vision/radar classifiers can be neural predicates coupled with aviation regulations as symbolic predicates for joint training.

### B.3 Logic Tensor Networks (LTN)
**Logic Tensor Networks (LTN)** fuse real-valued (fuzzy) logic with deep learning computation graphs.
* **Core capabilities:** T-norms turn Boolean formulas into differentiable losses; TensorFlow or PyTorch backends supported.
* **Use in this book:** Primary practice vehicle for “logic as loss” (Chapter 8). Encode CCAR-style separation constraints as formulas penalizing trajectory predictors during training.

### B.4 PyTorch Geometric (PyG)
**PyTorch Geometric** is the dominant PyTorch extension for graph neural networks.
* **Core capabilities:** Sparse/dynamic graph kernels, GCN/GAT/GraphSAGE-style message passing, temporal and heterogeneous graph utilities.
* **Use in this book:** Part IV (dynamic coordination)—foundation for Chapter 12’s graph-driven multi-agent conflict models; temporal attention on high-rate TKG snapshots for millisecond-scale sensing.

### B.5 RDFLib / OWLReady2 / Neo4j / GraphDB
These tools cover the KG lifecycle from ontology modeling to graph storage.
* **RDFLib & OWLReady2:** Native Python semantic-web stacks. RDFLib reads/writes/queries RDF; OWLReady2 loads and reasons over OWL ontologies in Python—useful for SkyKG concept and rule layers (Chapter 6).
* **Neo4j:** Industrial property-graph database with Cypher—fast traversals for dynamic traffic workloads.
* **GraphDB:** Enterprise RDF/SPARQL store with forward-chaining inference (OWL 2 RL/QL fragments)—a natural backend for deterministic static compliance checks (Chapter 10, rule-query channel).

### B.6 LLM + KG Integration Stacks
Middleware connecting large models to structured knowledge is central to GraphRAG (Chapters 10 and 22).
* **LangChain & LlamaIndex:** Mainstream LLM orchestration frameworks with loaders for graph stores, SPARQL/Cypher generation, and multi-hop subgraph retrieval.
* **Microsoft GraphRAG:** Microsoft’s open KG-RAG stack emphasizing hierarchical entities and global summaries—helpful for fleet-level situational questions beyond local chunk retrieval.

### B.7 Streaming Inference and Edge Deployment
To bridge the compute–latency gap (Chapter 18) and deploy in the field, use stream processing and edge runtimes.
* **Apache Flink / Kafka:** High-throughput streaming and messaging—ingest ~10 Hz ADS-B feeds and drive event-driven TKG updates.
* **TensorRT & ONNX Runtime:** Quantization and optimized inference—deploy trained GNNs and light perception nets to 5G MEC or onboard Jetson-class devices for low-latency interventions.
