---
type: raw
source_type: paper
source_url: https://www.alphaxiv.org/abs/2605.18747
date_ingested: 2026-05-22
tags:
  - ai
  - agents
  - coding
  - llm
  - survey
status: processed
compiled_at: 2026-05-23
compiled_to: "[[src_code-as-agent-harness-arxiv-2605-18747.md]]"
---

# Code as Agent Harness

## Metadata

- **Source:** alphaXiv / arXiv
- **URL:** https://www.alphaxiv.org/abs/2605.18747
- **arXiv ID:** 2605.18747
- **Date Ingested:** 2026-05-22
- **Paper Type:** Survey / Position Paper

## Authors & Institutions

**Core Contributors:**
- Xuying Ning
- Katherine Tieu  
- Dongqi Fu
- Tianxin Wei
- Zihao Li
- Yuanchen Bei

**Affiliations:**
- University of Illinois Urbana-Champaign
- Meta
- Stanford University

## Abstract

This paper reframes the role of code within LLM-based agentic systems from a mere generated artifact to a foundational **operational substrate** — what the authors term "Code as Agent Harness."

The core thesis: Code is no longer just an output target for LLMs (demonstrating coding capability), but becomes the **medium for agent intelligence** itself — spanning reasoning, action, environment modeling, and execution-based verification.

### Key Concepts

**Agent-Initiated Code Artifacts:**
Interactive code objects that agents create, execute, observe, revise, and share within a task execution loop. These artifacts sit between:
- LLM's internal capabilities (reasoning, planning)
- Pre-defined system infrastructure (harness layer)

**Why Code as Substrate:**
| Property | Benefit for Agents |
|----------|-------------------|
| Executable | Actions become concrete, testable |
| Inspectable | Intermediate steps are transparent |
| Stateful | Task progress persists across steps |
| Verifiable | Correctness can be checked via execution |

**vs. Traditional View:**
- **Old:** Code = output of LLM coding capability
- **New:** Code = operational foundation connecting model outputs to long-horizon actions

## Research Landscape Position

The paper synthesizes disparate research efforts into a unified taxonomy:

1. **Code for Reasoning** — Externalizing computation, symbolic reasoning
2. **Code for Action** — Executable policies (robots, GUI agents)
3. **Code for Environment Modeling** — State representation, dynamics, feedback
4. **Code for Verification** — Execution-based validation

## Motivation

**The Bottleneck:** Agent autonomy is limited not just by model reasoning, but by the **reliability of the connection** between model outputs and persistent execution.

**Code as Solution:**
- Pure text reasoning: unreliable for symbolic computation, hard to verify, no persistence
- Code: executable, inspectable, stateful — enabling reliable closed-loop behavior

## Three-Layer Taxonomy

The paper organizes research around **three interconnected layers**, reflecting how code's operational role progresses within an agent loop:

### Layer 1: Harness Interface — Code as Connection

How code forms the fundamental link between an agent and its capabilities:

**1.1 Code for Reasoning**
- Externalizes internal logic into **verifiable computation**
- Uses external interpreters, solvers, execution traces to check and refine reasoning
- Enables symbolic reasoning beyond LLM's internal limitations

**1.2 Code for Acting**  
- Generated programs as **executable policies**
- Tool calls, reusable skills for interacting with:
  - Embodied environments (robots)
  - GUI environments
  - Software/API environments

**1.3 Code for Environment Modeling**
- Program states, repositories, traces, simulators, tests represent:
  - **World state** — current situation
  - **Dynamics** — how environment changes
  - **Feedback signals** — results of actions

### Layer 2: Harness Mechanisms — Reliability Over Time

How code-harnessed agents maintain reliability across long-horizon tasks:

**2.1 Planning for Agent Harness**
Planning as **harness control layer** — structuring how agents externalize intent into executable steps:

| Planning Paradigm | Description | Examples |
|-------------------|-------------|----------|
| **Linear Decomposition** | Sequential step generation | Self-Planning |
| **Structure-Grounded** | Grounding in explicit task structures | CodePlan |
| **Search-Based** | Exploring multiple solution paths | CodeTree |
| **Orchestration-Based** | Coordinating specialized agent roles | MapCoder |

**2.2 Memory and Context Engineering**
Managing tension between **limited context windows** and **continuously expanding task states**:

| Memory Type | Function | Use Case |
|-------------|----------|----------|
| **Working Memory** | Current task trajectory | Immediate execution state |
| **Semantic Memory** | Retrieve repository evidence | Code understanding |
| **Experiential Memory** | Store reusable experiences | Skill learning |
| **Long-Term Memory** | Preserve validated knowledge | Persistent expertise |
| **Multi-Agent Memory** | Synchronize shared state | Distributed coordination |

**Context Compaction & State Offloading:**
- Summarizing information to fit context limits
- Offloading full-fidelity artifacts to external storage

**2.3 Tool Use for Agent Harness**
Tools as **action and observation layer**, expanding capabilities and exposing feedback:

| Tool Category | Purpose | Examples |
|---------------|---------|----------|
| **Function-Oriented** | API calls and operations | Code execution |
| **Environment-Interaction** | Development environment access | File systems, repos |
| **Verification-Driven** | Post-generation validation | Linters, tests |
| **Workflow-Orchestration** | Complex workflow coordination | CI/CD pipelines |

**2.4 Harness Control (Plan-Execute-Verify Loop)**
Transforming debugging into **control process for state transitions**:

| Control Phase | Function | Mechanism |
|---------------|----------|-----------|
| **Planning as Contract Formation** | Define intended changes | Explicit pre-conditions |
| **Sandboxed Execution** | Isolated environment testing | Containerized runs |
| **Permissioned State Transition** | Access-controlled modifications | Role-based permissions |
| **Deterministic Verification** | Objective correctness checking | Linters, tests, type checkers |

**2.5 Agentic Harness Engineering**
The harness itself as object of **analysis and optimization**:

| Optimization Mechanism | Description | Examples |
|------------------------|-------------|----------|
| **Deep Telemetry** | Structured traces diagnose failures | Execution logging |
| **Evolution Agent** | Meta-agent proposes harness revisions | Self-improvement loops |
| **Governed Harness Mutation** | Safety-critical change management | Code review for harness |

### Layer 3: Scaling the Harness — Multi-Agent Systems

How shared code artifacts support coordination, review, and collective verification:

**3.1 Improved Coding Support through Multi-Agent Collaboration**

*Functional Role Specialization:*
- **Programmer** — code generation
- **Tester** — test writing and execution  
- **Reviewer** — code review and critique
- **Architect** — high-level design decisions
- Examples: ChatDev, MetaGPT, AgentCoder

*Diverse Interaction Modes:*
| Mode | Description | Benefit |
|------|-------------|---------|
| **Collaborative Synthesis** | Joint creation | Combined expertise |
| **Critique and Repair** | Identify and fix issues | Quality assurance |
| **Adversarial Validation** | Stress-testing | Robustness |
| **Reasoning Debate** | Multiple viewpoints | Comprehensive analysis |

*Optimized Workflow Topologies:*
- **Predefined chains** — waterfall structure
- **Cycles** — agile iteration
- **Hierarchies** — layered decomposition
- **Dynamic/adaptive** — evolving with task complexity
- Examples: EvoMAC, FlowReasoner

**3.2 Execution Feedback and Shared-Harness Synchronization**

*Execution Feedback Types:*
| Feedback Type | Source | Use |
|---------------|--------|-----|
| **Compiler/syntax errors** | Static analysis | Immediate correction |
| **Test pass/fail** | Test suites | Functional validation |
| **Fuzzer crash traces** | Dynamic testing | Edge case discovery |
| **Static analysis warnings** | Linters | Code quality |
| **Performance profiling** | Runtime monitoring | Optimization |
| **Fine-grained simulation** | Simulators | Safe exploration |
- Examples: AgentCoder, AutoSafeCoder, MAGE

*Shared-Harness Synchronization Mechanisms:*
| Mechanism | Description | Use Case |
|-----------|-------------|----------|
| **Sequential Handoff** | Ordered agent transitions | Pipeline workflows |
| **Shared Blackboards** | Centralized state repository | Common knowledge |
| **Parallel Branches with Merge** | Concurrent development | Feature branches |
| **Structured Context Scheduling** | Time-sliced access | Resource sharing |
| **Hierarchical Memory** | Multi-level state | Complex hierarchies |
| **Agent Pool Scaling** | Dynamic agent allocation | Elastic workloads |

**3.3 Shared Code-Centric Harness Substrate (Position)**
Formal, persistent representations of **shared code state**:

| Representation Type | Formality | Examples |
|---------------------|-----------|----------|
| **Implicit** | Informal conventions | Ad-hoc coordination |
| **Repository-based** | Version control | Git workflows |
| **Execution-based** | Runtime state | Live debugging |
| **Blackboard** | Formal shared substrate | Multi-agent shared memory |

## Methodology

The paper employs a **comprehensive literature survey** methodology:

1. **Conceptual Formalization:**
   - Introduce "code as agent harness" perspective
   - Distinguish "agent-initiated code artifacts" from:
     - Model-internal capabilities
     - System-provided harness infrastructure
   - Emphasize code's role as executable, inspectable, stateful medium

2. **Systematic Taxonomy Construction:**
   - Three-layer hierarchical organization
   - Reflects progression of code's operational role
   - Synthesizes disparate research into coherent framework

3. **Literature Synthesis:**
   - Cross-cutting analysis of existing work
   - Identification of gaps and opportunities
   - Roadmap for future development

## Key Distinctions

**Code Artifacts sit between:**
```
LLM Internal Capabilities ←→ Agent-Initiated Code Artifacts ←→ System Harness Infrastructure
   (reasoning, planning)        (executable, inspectable)         (tools, sandboxes)
```

**Research Contribution:**
- Not introducing new techniques
- Providing **unified conceptual framework**
- Enabling systematic comparison and roadmap development

## Application Domains

The paper connects its taxonomy to **five key application domains**, demonstrating practical instantiation of the "code as agent harness" paradigm:

### Domain 1: Coding Assistants
- **Code generation** from natural language specifications
- **Interactive debugging** with execution feedback
- **Program synthesis** via iterative refinement
- **Repository-level reasoning** with codebase understanding

### Domain 2: GUI/OS Agents
- **Desktop automation** through programmatic control
- **Web agents** navigating browser environments
- **Mobile agents** interacting with app interfaces
- **Cross-application workflows** via shared harness

### Domain 3: Embodied Agents
- **Robot control policies** generated as executable code
- **Physical skill learning** through trial and execution
- **World models** represented as programmable simulations
- **Sensorimotor loops** with code-based state tracking

### Domain 4: Scientific Discovery
- **Experiment design** as executable protocols
- **Data analysis pipelines** with reproducible steps
- **Hypothesis testing** via programmatic verification
- **Literature synthesis** through structured extraction

### Domain 5: Personalization & Recommendation
- **User modeling** via executable preference programs
- **Recommendation policies** as learnable code
- **Adaptive interfaces** through runtime modification
- **Behavioral simulation** with programmable user agents

## Main Findings & Results

### 5.1 Harness Interface: Three Core Functions

#### A. Code for Reasoning
Transforming internal model logic into **executable, verifiable computation**:

**Program-Delegated Reasoning:**
- LLMs generate programs for external interpreters
- Improves reliability in symbolic/arithmetic tasks
- Examples: Program-of-Thoughts, PAL (Program-Aided Language models)

**Formal Verification & Symbolic Interfaces:**
- Formal languages (Lean, Isabelle) for verifiable proof search
- Hybrid neural-symbolic methods with persistent representations
- Examples: DeepSeek-Prover, CodeSteer

**Iterative Code-Grounded Reasoning:**
- Closed-loop process with execution traces and runtime feedback
- Learning from failures to refine reasoning
- Examples: NExT, CodePRM, RLEF

#### B. Code for Acting
Translating high-level intent into **grounded, executable operations**:

**Grounded Skill Selection:**
- Mapping language intent to reusable skill libraries
- Considering environmental and physical constraints
- Examples: SayCan, KnowNo

**Programmatic Policy Generation:**
- Code directly materializes executable policies
- Robot control, GUI automation, API interactions
- Examples: Code as Policies, RoboCodeX

**Lifelong Code-Based Agents:**
- Executable interfaces persist and evolve over time
- Accumulating reusable skill memories
- Examples: Voyager, UI-Voyager

#### C. Code for Environment Modeling
Representing environments as **programmatic, inspectable structures**:

**Structured World Representations:**
- Class hierarchies, room programs, renderable HTML
- Explicit manipulation and inspection of world state
- Examples: ViStruct, Code2World

**Execution-Trace World Modeling:**
- Learning environment dynamics from interaction traces
- Predictive models of future states
- Examples: Code World Model, WorldCoder

**Code-Grounded Evaluation Environments:**
- Sandboxes, unit tests, simulators as objective interfaces
- Measuring agent behavior and interaction quality
- Examples: SWE-bench, AgentBench, InterCode

**Verifiable Environment Construction:**
- Programmatic synthesis, scaling, validation
- Defining state transitions, tool affordances, verifiers
- Examples: SWE-smith, EnvScaler

### 5.2 Harness Mechanisms: Maintaining Reliability

| Mechanism | Key Finding | Representative Methods |
|-----------|-------------|----------------------|
| **Planning** | Decomposition + structural grounding essential | Task graphs, workflow orchestration |
| **Memory** | Multiple memory types needed (working, semantic, experiential, long-term) | Context windows, vector stores, episodic memory |
| **Tool Use** | Governed interfaces prevent uncontrolled execution | API schemas, permission systems |
| **Control** | Plan-Execute-Verify loop enables self-correction | Contract formation, sandboxed execution |
| **Optimization** | Harness can evolve through telemetry and mutation | Evolution agents, governed self-improvement |

### 5.3 Scaling: Multi-Agent Coordination

**Shared Code-Centric Substrate:**
- Unified view of shared program environment
- Harness state convergence across distributed agents
- Blackboard architectures, structured context scheduling

### 5.4 Open Challenges & Future Directions

The paper identifies critical **"harness engineering"** challenges:

1. **Evaluation:** How to measure harness effectiveness beyond task success
2. **Semantic Verification:** Ensuring code correctness beyond syntactic validity  
3. **Self-Evolving Harnesses:** Autonomous improvement of the harness itself
4. **Transactional State:** Atomic operations across distributed agent systems
5. **Human Oversight:** Maintaining meaningful human control in autonomous systems
6. **Multimodal Integration:** Extending code-centric approach to vision, audio, etc.

**Harness-State Convergence:**
Criteria for stopping iteration and determining completion:

| Convergence Criterion | Basis | When Applied |
|----------------------|-------|--------------|
| **Correctness (test-gated)** | Objective test results | Functional validation |
| **Security** | Security checks passed | Safety-critical systems |
| **Performance** | Performance metrics met | Optimization targets |
| **Score-based** | Quantitative thresholds | Benchmark evaluations |
| **Consensus** | Multi-agent agreement | Distributed decision-making |
| **Implicit** | Heuristic termination | Simple/complex tasks |

Moving beyond implicit termination to **objectively grounded convergence**.

---

## Significance and Potential Impact

### Conceptual Framing: "Code as Agent Harness"

The paper's core contribution is providing a **unified and systematic understanding** of code's evolving role in AI agent systems:

**Paradigm Shift:**
```
Old View: Code = output of LLM coding capability
New View: Code = executable, inspectable, stateful operational substrate
```

### Multi-Faceted Impact

**1. Foundation for Reliable AI Agents**
- Emphasizes the **harness layer** — software surrounding the LLM
- Addresses **system-level robustness** beyond base model capabilities
- Enables **long-horizon, adaptable** agent behavior

**2. Structured Research Roadmap**
- **Three-layered taxonomy** for categorizing existing work
- Identifying **gaps** and guiding **future development**
- Promoting **holistic understanding** of agent architectures

**3. Bridging AI and Software Engineering**
Deep integration of software engineering concepts:
- Version control
- Testing and debugging  
- CI/CD pipelines
- Formal methods

**Fostering interdisciplinary collaboration** and adoption of robust practices.

**4. Impact on Application Domains**

| Domain | Application | Benefit |
|--------|-------------|---------|
| **Coding Assistants** | Autonomous coding tools | Self-driving development |
| **GUI/OS Agents** | Generalist computer-using agents | Automated workflows |
| **Embodied Agents** | Verifiable robotic policies | Safe physical interaction |
| **Scientific Discovery** | Self-driving laboratories | Automated experimentation |
| **Personalization** | Adaptive recommendation systems | Dynamic user modeling |

**5. Critical Open Problems Agenda**

Key challenges identified for future research:

| Challenge | Description | Importance |
|-----------|-------------|------------|
| **Harness-level Evaluation** | Measuring harness effectiveness | Beyond task success |
| **Semantic Verification** | Correctness beyond executable feedback | Logical validity |
| **Regression-free Self-Evolution** | Safe harness self-improvement | Reliability preservation |
| **Transactional Shared State** | Atomic distributed operations | Consistency guarantees |
| **Human-in-the-Loop Safety** | Meaningful human control | Safety and oversight |

**6. Emergence of "Harness Engineering"**

Advocating for **new scientific discipline**:
- Focus: Designing, measuring, optimizing operational substrates
- Goal: Turn stateless models into functional, governed, verifiable agents
- Outcome: New tools, methodologies, benchmarks for agent systems

### Summary Vision

> "Code is central to not just what agents produce, but **how they function, interact, and evolve reliably** in complex environments."

This framework influences the **next generation of AI agent design and engineering practices**.

## Keywords

#llm-agents #code-generation #ai-systems #agent-architecture #survey #multi-agent #executable-reasoning
