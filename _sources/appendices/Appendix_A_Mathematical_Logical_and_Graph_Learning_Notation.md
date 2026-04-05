# Appendix A — Mathematical, Logical and Graph Learning Notation
> This appendix follows the book outline’s “Appendix A: Notation for mathematics, logic, and graph learning.” It unifies notation for logic, graph learning, statistical certification, and system architecture so readers can cross-reference chapters quickly.

This appendix does not aim for the most abstract axiomatic treatment; it serves the book’s narrative. It explains symbols that recur in KG-driven neuro-symbolic reasoning, temporal relational graphs, conformal prediction and online certification, and cloud–edge deployment. To avoid semantic drift of the same symbol across chapters, we follow: (1) prefer the most common, intuitive notation used in the main text; (2) if a symbol may differ by context, the “Notes” column limits scope; (3) for rule templates, graph tensors, and calibration quantities, give both formal meaning and engineering reading to link theory and implementation.

---

## A.1 Logical Symbols and Common Rule Templates

This section collects notation for propositional logic, first-order logic, rule representation, constraints, and explanation chains. Neuro-symbolic systems mix formal logic and engineering rules, so we keep both **strict logical symbols** and **rule-template** forms.

### A.1.1 Basic Logical Symbols

| Symbol | English name | Meaning | Notes |
|---|---|---|---|
| $P, Q, R$ | Propositional variables | Atomic true/false propositions | Common in propositional examples |
| $\lnot P$ | Negation | $P$ is false | Read as “not $P$” |
| $P \wedge Q$ | Conjunction | Both $P$ and $Q$ hold | Logical AND |
| $P \vee Q$ | Disjunction | At least one of $P$, $Q$ holds | Logical OR |
| $P \rightarrow Q$ | Implication | If $P$ then $Q$ | Ubiquitous in rule systems |
| $P \leftrightarrow Q$ | Biconditional | $P$ if and only if $Q$ | Bidirectional constraints |
| $\top$ | Tautology | Always true | Logical construction |
| $\bot$ | Contradiction | Always false | Contradiction or empty conclusion |
| $\forall x$ | Universal quantifier | For all $x$ | First-order logic |
| $\exists x$ | Existential quantifier | There exists $x$ | First-order logic |
| $x, y, z$ | Individual variables | Objects, entities, or nodes | e.g., UAVs, missions, airspace |
| $c$ | Constant | A fixed individual | A specific UAV or corridor |
| $f(x)$ | Function term | Object mapped to object | e.g., $\mathrm{location}(u)$ |
| $\mathrm{Predicate}(x)$ | Predicate | Property or relation | e.g., $\mathrm{UAV}(x)$, $\mathrm{Conflict}(x,y)$ |
| $=$ | Equality | Terms denote the same object | Entity identity |
| $\neq$ | Inequality | Terms differ | Common in constraints |

### A.1.2 Common Knowledge-Representation Templates

| Template | Form | Meaning | Typical scenario |
|---|---|---|---|
| Type assertion | $\mathrm{Type}(x)$ | $x$ has a type or property | $\mathrm{UAV}(u)$, $\mathrm{EmergencyMission}(m)$ |
| Binary relation | $\mathrm{Rel}(x, y)$ | Relation between $x$ and $y$ | $\mathrm{locatedIn}(u, z)$ |
| Conditional rule | $A(x) \wedge B(x) \rightarrow C(x)$ | If $A$ and $B$ then $C$ | Static risk rules |
| Multi-entity rule | $A(x,y) \wedge B(y,z) \rightarrow C(x,z)$ | Chain entities to infer new relation | Path reasoning on graphs |
| Constraint rule | $A(x) \rightarrow \lnot B(x)$ | If $A$ then $B$ must not hold | Compliance, conflict resolution |
| Priority rule | $\mathrm{HighPriority}(x) \wedge \mathrm{Conflict}(x,y) \rightarrow \mathrm{Yield}(y)$ | Lower priority yields in conflict | UAM coordination |
| Exception rule | $A(x) \wedge \lnot\mathrm{Exception}(x) \rightarrow B(x)$ | Default rule unless excepted | Regulatory modeling |
| Explanation template | $\mathrm{Fact} \wedge \mathrm{Rule} \rightarrow \mathrm{Conclusion}$ | Organize NL explanation chains | SkyKG-style systems |

### A.1.3 Engineering Rule Templates

| Template name | Rule form | Engineering meaning |
|---|---|---|
| Alert trigger | `IF condition THEN alert(level)` | Raise alert when condition holds |
| Risk tiering | $\texttt{IF score} \geq \tau_h \texttt{ THEN high\_risk}$ | Map score to risk band |
| Compliance check | `IF forbidden(zone, u) THEN reject(path)` | Reject illegal paths |
| Candidate action | `IF conflict(u,v) THEN generate(action_set)` | Propose de-conflict actions |
| Human review | $\texttt{IF confidence} < \tau_c \texttt{ THEN human\_review}$ | Escalate when uncertain |
| Certification downgrade | `IF drift_detected THEN downgrade(cert_level)` | Lower assurance after drift |

### A.1.4 Evidence and Explanation Chains

| Symbol | Meaning | Notes |
|---|---|---|
| $E$ | Evidence set | From graph queries, sensors, logs |
| $R$ | Rule set | Rule base, ontology, policies |
| $C$ | Conclusion set | Risk labels, compliance outcomes, explanations |
| $E \vdash C$ | $E$ proves $C$ | Syntactic “$E$ derives $C$” |
| $E, R \vdash C$ | Derive $C$ from $E$ under $R$ | Core neuro-symbolic form |
| $\pi$ | Reasoning path / explanation chain | Fact-to-conclusion trace |
| $\mathrm{support}(c)$ | Supporting evidence for $c$ | Faithfulness of explanation |
| $\mathrm{trace}(c)$ | Inference trace for $c$ | Audit and review |

---

## A.2 Graph Neural Networks and Temporal Graph Notation

Notation for KG embedding, temporal relational graphs, GNNs, relational attention, dynamic conflict detection, and coordination. Some symbols carry both generic graph meaning and UAM-specific reading.

### A.2.1 Graphs and Knowledge Graphs

| Symbol | Meaning | Notes |
|---|---|---|
| $G = (V, E)$ | Graph | $V$ nodes, $E$ edges |
| $V$ | Node set | UAVs, missions, airspace, rule nodes, … |
| $E$ | Edge set | Interaction, constraint, adjacency, dependency, … |
| $v_i$ | Node $i$ | Single entity |
| $e_{ij}$ | Edge $i \to j$ | Directed, typed |
| $A$ | Adjacency matrix | Matrix view of structure |
| $X$ | Node feature matrix | Inputs per node |
| $R$ | Relation-type set | Edge types in a KG |
| $(h, r, t)$ | Triple | Head, relation, tail |
| $\mathrm{KG}$ | Knowledge graph | Explicit relational knowledge |
| $\mathrm{TKG}$ | Temporal knowledge graph | Time-varying KG |
| $G_t$ | Graph at time $t$ | Snapshot in dynamic graphs |
| $\Delta G_t$ | Graph increment | Change from $t{-}1$ to $t$ |

### A.2.2 Node, Edge, and Relation Features

| Symbol | Meaning | Notes |
|---|---|---|
| $x_i$ | Raw features of node $i$ | Position, speed, battery, mission state, … |
| $h_i^{(l)}$ | Hidden state of node $i$ at layer $l$ | GNN layer output |
| $h_i^{(0)}$ | Initial node representation | Usually from $x_i$ |
| $r_{ij}$ | Relation type on $(i,j)$ | Conflict, adjacency, dependency, priority, … |
| $w_{ij}$ | Edge weight | Risk, distance, propagation strength |
| $\tau_{ij}$ | Timestamp or delay on edge | Temporal graphs |
| $z_i$ | Node embedding | Often interchangeable with $h_i$ |
| $z_{ij}$ | Edge / relation embedding | Relation-aware models |

### A.2.3 GNN and Attention Notation

| Symbol | Meaning | Notes |
|---|---|---|
| $\mathcal{N}(i)$ | Neighbors of $i$ | Basis of message passing |
| $m_{ij}$ | Message $j \to i$ | Intermediate message |
| $M^{(l)}$ | Layer-$l$ message aggregate | Sum, mean, attention-weighted, … |
| $U^{(l)}$ | Layer-$l$ update map | Maps aggregate to new state |
| $\alpha_{ij}$ | Attention weight | Influence of $j$ on $i$ |
| $W^{(l)}$ | Layer-$l$ weight matrix | Conv / attention parameters |
| $\sigma(\cdot)$ | Activation | ReLU, sigmoid, tanh, … |
| $\mathrm{AGG}(\cdot)$ | Aggregation operator | Sum, mean, max, … |
| $\mathrm{CONCAT}(\cdot)$ | Concatenation | Multi-head or multi-source fusion |
| $\mathrm{HEAD}_k$ | Attention head $k$ | Multi-head attention |
| $\beta_{ij}^t$ | Temporal relational attention | Time-aware edge weights |

### A.2.4 Temporal Graphs and Dynamic Reasoning

| Symbol | Meaning | Notes |
|---|---|---|
| $t$ | Time step / timestamp | Discrete or continuous |
| $T$ | Window length | Sliding windows |
| $S_t$ | System state at $t$ | Graph + rule state |
| $H_t$ | History | $H_t = \{G_{t-k}, \ldots, G_t\}$ |
| $\phi_t$ | Time encoding | Sinusoidal, relative time, … |
| $P(\mathrm{conflict}_{ij}^{t+\Delta})$ | Future conflict probability | Risk for pair $(i,j)$ |
| $y_t$ | Ground-truth label at $t$ | e.g., conflict occurred |
| $\hat{y}_t$ | Prediction at $t$ | Risk score or class |
| $\mathrm{CDR}$ | Conflict detection rate | |
| $\mathrm{FAR}$ | False alert rate | |
| $F_1$ | F1 score | Precision–recall balance |
| $\mathrm{latency}$ | Inference latency | Real-time metric |

### A.2.5 Coordination, De-confliction, and Path Reasoning

| Symbol | Meaning | Notes |
|---|---|---|
| $\pi_u$ | Path / plan of agent $u$ | Route or action sequence |
| $\pi_u^*$ | Optimized path | After de-confliction |
| $a_t$ | Action at $t$ | Reroute, slow down, wait, corridor switch, … |
| $A_t$ | Candidate actions at $t$ | Filtered by rules and graph |
| $c_t$ | Conflict set | Current or predicted conflicts |
| $\mathrm{resolve}(c_t)$ | Conflict-resolution map | Conflicts $\to$ suggested actions |
| $\mathrm{reward}_t$ | RL immediate reward | Path / coordination learning |
| $J(\pi)$ | Path cost | Time, risk, energy, rule penalties |

---

## A.3 Conformal Prediction and Statistical Calibration

Notation for trustworthy certification, uncertainty, conformal prediction, online monitoring, and drift. We distinguish raw model outputs, calibrated scores, certified sets/intervals, and online monitors—reflecting the move from explanatory to certifiable outputs.

### A.3.1 Basic Probability and Statistics

| Symbol | Meaning | Notes |
|---|---|---|
| $X$ | Input random variable | Sample, graph state, evidence structure |
| $Y$ | Output random variable | Label, risk class, conclusion |
| $(x_i, y_i)$ | Sample $i$ | Calibration or test |
| $\mathcal{D}_{\mathrm{train}}$ | Training set | Fit the model |
| $\mathcal{D}_{\mathrm{cal}}$ | Calibration set | Conformal / calibration |
| $\mathcal{D}_{\mathrm{test}}$ | Test / online stream | Evaluation and deployment |
| $\hat{f}(x)$ | Predictor | Scores, probabilities, labels |
| $\hat{p}(y \mid x)$ | Predicted class probabilities | |
| $P(\cdot)$ | Probability | Event probability |
| $\mathbb{E}[\cdot]$ | Expectation | |
| $\mathrm{Var}(\cdot)$ | Variance | |
| $\alpha$ | Significance level | e.g., $0.05$ |
| $1-\alpha$ | Confidence / coverage level | Conformal coverage target |

### A.3.2 Conformal Prediction

| Symbol | Meaning | Notes |
|---|---|---|
| $s_i$ | Nonconformity score for sample $i$ | |
| $S(x,y)$ | Nonconformity function | Residual, neg-log-prob, rule violation, … |
| $q_{1-\alpha}$ | $(1-\alpha)$-quantile threshold | From calibration scores |
| $\Gamma_\alpha(x)$ | Conformal prediction set | Set with coverage guarantee |
| $C(x)$ | Prediction interval / set | Often synonymous with $\Gamma_\alpha(x)$ |
| $\mathrm{coverage}$ | Empirical coverage | Fraction of truths in predicted sets |
| $\mathrm{set\_size}$ | Prediction set size | Efficiency in set prediction |
| $\mathrm{residual}_i$ | Residual | Common in regression |
| $\hat{y}^-,\; \hat{y}^+$ | Lower / upper bounds | Interval endpoints |

### A.3.3 Calibration and Trust Scores

| Symbol | Meaning | Notes |
|---|---|---|
| $\mathrm{conf}(x)$ | Confidence score | Model-reported |
| $\mathrm{calib}(x)$ | Post-calibration confidence | |
| $\mathrm{score}_{\mathrm{faith}}$ | Explanation faithfulness | Static explanation chains |
| $\mathrm{score}_{\mathrm{align}}$ | Rule-alignment score | Match to rules |
| $\mathrm{score}_{\mathrm{cov}}$ | Evidence coverage score | How much evidence is cited |
| $\mathrm{score}_{\mathrm{cert}}$ | Composite certification score | After statistical wrapping |
| $\mathrm{RAR}$ | Rule alignment rate | |
| $\mathrm{UCR}$ | Unsupported claim rate | |
| $\mathrm{ECE}$ | Expected calibration error | |
| $\mathrm{Brier}$ | Brier score | Probabilistic quality |

### A.3.4 Online Monitoring and Drift

| Symbol | Meaning | Notes |
|---|---|---|
| $p_t$ | $p$-value or calibration stat at $t$ | Monitor input |
| $M_t$ | Martingale value at $t$ | |
| $M_0 = 1$ | Initial martingale | Common init |
| $\mathrm{drift}_t$ | Drift flag/state at $t$ | Boolean or graded |
| $\delta_t$ | Drift strength | Continuous or discrete |
| $\mathrm{alarm}_t$ | Alarm at $t$ | Anomaly trigger |
| $\tau_d$ | Drift threshold | Enter conservative mode |
| $\tau_a$ | Alarm threshold | Downgrade or human review |
| $\mathrm{seq}_t$ | Output sequence up to $t$ | Sequence consistency |
| $\mathrm{OOD}(x)$ | Out-of-distribution score | |

### A.3.5 Dynamic Risk Prediction and Certified Wrappers

| Symbol | Meaning | Notes |
|---|---|---|
| $r_t$ | Raw risk score at $t$ | Direct model output |
| $\tilde{r}_t$ | Calibrated risk | After calibration |
| $I_t = [l_t, u_t]$ | Risk interval | Certified bounds |
| $A_t^{\mathrm{cert}}$ | Certified action set | Actions meeting trust criteria |
| $\mathrm{level}_t$ | Certification level | High / medium / needs review |
| $\mathrm{safe}_t$ | Declared safety state | Output-layer safety label |
| $\mathrm{human\_review}_t$ | Human-review flag | High risk or drift |

---

## A.4 System Architecture and Complexity Analysis

Notation for cloud–edge collaboration, distributed graph reasoning, spatiotemporal partitioning, throughput, fault tolerance, and complexity—supporting the systems part of the book (SkyGrid, edge inference, concurrent engines, city-scale deployment).

### A.4.1 System Architecture

| Symbol | Meaning | Notes |
|---|---|---|
| $\mathcal{E}$ | Edge node set | |
| $\mathcal{C}$ | Cloud node set | |
| $e_k$ | Edge node $k$ | May own subgraph(s) |
| $c_m$ | Cloud node $m$ | Global coordination |
| $\mathcal{P}$ | Set of partitions | |
| $P_k$ | Partition $k$ | Local domain |
| $B_{ij}$ | Boundary buffer | Overlap / shared boundary |
| $\mathrm{sync}(P_i, P_j)$ | Partition sync | Boundary state |
| $\mathrm{sched}(\cdot)$ | Scheduler | Tasks, events, resources |
| $\mathrm{queue}_k$ | Task queue at node $k$ | Event-driven execution |

### A.4.2 Spatiotemporal Partitioning and Propagation

| Symbol | Meaning | Notes |
|---|---|---|
| $G_t^k$ | Subgraph $k$ at time $t$ | Local spatiotemporal state |
| $\mathrm{cut}(E)$ | Cut edge set | Edges split by partition |
| $\mathrm{boundary}(v)$ | Boundary flag for $v$ | On partition border |
| $\mathrm{propagate}(c, P_i \!\rightarrow\! P_j)$ | Cross-partition conflict propagation | |
| $\mathrm{load}(P_k)$ | Load of partition $k$ | Events, edges, inferences |
| $\mathrm{hotspot}(P_k)$ | Hotspot flag | High local load |
| $\mathrm{rebalance}(P_i, P_j)$ | Load rebalance | Migration / repartition |

### A.4.3 Parallel Reasoning and Complexity

| Symbol | Meaning | Notes |
|---|---|---|
| $N$ | Total entities / nodes | Scale analysis |
| $M$ | Total edges | |
| $K$ | Number of partitions / workers | Context-dependent |
| $L$ | Model depth | GNN or reasoning depth |
| $d$ | Embedding dimension | |
| $T$ | Time steps / window length | Dynamic graphs |
| $O(\cdot)$ | Asymptotic notation | |
| $O(N+M)$ | Linear graph traversal | |
| $O(K^{-1})$ | Ideal parallel scaling trend | Under balanced load |
| $\mathrm{speedup}(K)$ | Parallel speedup | vs. single node |
| $\mathrm{util}_k$ | Resource utilization at $k$ | CPU/GPU/memory |

### A.4.4 Throughput, Latency, and Fault Tolerance

| Symbol | Meaning | Notes |
|---|---|---|
| $\mathrm{throughput}$ | Throughput | Events per unit time |
| $\mathrm{latency\_avg}$ | Average latency | |
| $\mathrm{latency\_tail}$ | Tail latency | e.g., P95/P99 |
| $\mathrm{qps}$ | Queries per second | |
| $\mathrm{eps}$ | Events per second | |
| $\mathrm{fail}_k$ | Failure event at $k$ | |
| $\mathrm{recover}_k$ | Recovery at $k$ | |
| $\mathrm{RTO}$ | Recovery time objective | |
| $\mathrm{RPO}$ | Recovery point objective | |
| $\mathrm{degrade\_mode}$ | Degraded operating mode | Conservative policy |
| $\mathrm{redundancy}$ | Redundancy factor | State/compute redundancy |

### A.4.5 Platform and Governance Interfaces

| Symbol | Meaning | Notes |
|---|---|---|
| $\mathrm{API}_{\mathrm{risk}}$ | Risk service API | Risk + explanation |
| $\mathrm{API}_{\mathrm{cert}}$ | Certification API | Trust level + monitor state |
| $\mathrm{API}_{\mathrm{coord}}$ | Coordination API | De-conflict suggestions |
| $\mathrm{log}_t$ | System log at $t$ | Audit, replay |
| $\mathrm{trace}_t$ | Evidence trace at $t$ | |
| $\mathrm{audit}(\cdot)$ | Audit function | Post hoc review |
| $\mathrm{policy}(\cdot)$ | Platform policy | Rules, permissions, routing |

---

## How to Use Appendix A

**First**, when the same symbol appears in multiple chapters, we keep a stable primary reading—e.g., $G_t$ as “graph state at time $t$,” $R$ as “rule set” or “relation-type set,” disambiguated by context.

**Second**, if a chapter specializes a symbol for a domain, the local definition wins but should not contradict this appendix.

**Third**, in engineering chapters, symbols like $\mathrm{API}_{\mathrm{risk}}$, $\mathrm{degrade\_mode}$, $\mathrm{load}(P_k)$ stress interfaces and system semantics over mathematical elegance.

**Fourth**, for reading paths: static cognition—see A.1 and A.3; dynamic coordination—A.2; systems foundation—A.4; trustworthy certification—A.3 with A.1.

**Fifth**, this appendix is a **unified notation table**, not a replacement for per-chapter problem statements. Chapters may introduce extra symbols; compatibility with this table is recommended.

## Appendix Summary

Appendix A organizes notation along four technical threads: logic and rule systems, GNNs and temporal graphs, conformal prediction and calibration, and system architecture with complexity analysis. The goal is cross-chapter consistency, not heavier formalism. For a book spanning knowledge representation, dynamic graph reasoning, trustworthy certification, and city-scale deployment, shared notation is both a convenience and a prerequisite for clear communication between theory and engineering.
