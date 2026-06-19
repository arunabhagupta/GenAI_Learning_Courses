# 🚀 The Complete GenAI Engineering Roadmap → Forward Deployed Engineer

> A self-paced, project-driven path from "strong Python, new to ML/AI" to building **end-to-end production GenAI systems** — RAG, Agents, MCP servers, Google ADK, and AWS Bedrock — across **two clouds**.
>
> **Two-environment strategy (important — read this):**
> - 🏢 **Professional / work:** **AWS Bedrock** is your production cloud (and likely provided by your office — use their account/credits for the paid cloud work).
> - 🏠 **Personal / learning:** **local-first and free** — **Ollama + LM Studio** for running models for free on your machine, with **LangChain + LangGraph** as your core framework and **RAG** as the through-line. Only reach for paid APIs/cloud when something genuinely can't be done locally.
> - **Cost rule:** *Free & local first → office-provided AWS for cloud → paid personal accounts only as a last resort.*
> **Last updated:** June 2026

---

## 📑 Table of Contents

1. [How to use this document](#0-how-to-use-this-document)
2. [Your goal & what an FDE actually is](#1-your-goal--what-an-fde-actually-is)
3. [The mental model: how the pieces fit together](#2-the-mental-model-how-the-pieces-fit-together)
4. [Prerequisites & environment setup](#3-prerequisites--environment-setup)
5. [The roadmap at a glance](#4-the-roadmap-at-a-glance)
6. [Phase 0 — ML/LLM foundations (no black boxes)](#phase-0--mlllm-foundations-no-black-boxes)
7. [Phase 1 — LLM Engineering Core](#phase-1--llm-engineering-core)
8. [Phase 2 — RAG mastery (deep)](#phase-2--rag-mastery-deep)
9. [Phase 3 — Agents: patterns & frameworks](#phase-3--agents-patterns--frameworks)
10. [Phase 4 — MCP: build servers & clients](#phase-4--mcp-build-servers--clients)
11. [Phase 5 — Google ADK](#phase-5--google-adk-agent-development-kit)
12. [Phase 6 — AWS Bedrock & AgentCore](#phase-6--aws-bedrock--agentcore)
13. [Phase 7 — Production: deploy, observe, evaluate, secure](#phase-7--production-deploy-observe-evaluate-secure)
14. [Phase 8 — Capstone & FDE readiness](#phase-8--capstone--fde-readiness)
15. [FDE competency checklist](#-fde-competency-checklist)
16. [Portfolio & GitHub strategy](#-portfolio--github-strategy)
17. [Staying current](#-staying-current)
18. [Quick-reference link library](#-quick-reference-link-library)

---

## 0. How to use this document

- **Order matters.** The phases are sequenced so each one unlocks the next. The single most important sequencing decision: **do not start ADK or AgentCore until you understand agent fundamentals (Phase 3).** Frameworks make no sense until you understand the patterns they implement.
- **Timeline is flexible**, so this plan uses **effort (hours)** and **"Definition of Done" checkpoints** instead of calendar weeks. Move at your own pace; the checkpoints tell you when you've truly absorbed a phase.
- **Build, don't just watch.** Every phase has a mandatory hands-on project. A passive video gives you ~10% retention; shipping a working artifact gives you the other 90% — and gives you a portfolio (critical for FDE roles).
- **One framework deeply > five shallowly.** You'll touch several frameworks (LangGraph, ADK, Strands, smolagents). Pick **LangGraph** or **ADK** as your "home" framework and go deep; treat the others as "read the docs, build one thing."
- ⭐ = highest-priority / do-not-skip resource. 🆓 = free. 💰 = paid.

---

## 1. Your goal & what an FDE actually is

A **Forward Deployed Engineer (FDE)** sits between your product/platform and a real customer's messy environment. You're not just building demos — you parachute into a client's world, understand their problem, and build a *working, integrated* solution fast. For GenAI specifically, FDE interviews and the job test for:

| FDE competency | What it means in practice |
|---|---|
| **Architectural judgment** | Choosing RAG vs fine-tuning vs agents; picking the right vector DB, retrieval strategy, orchestration boundary. |
| **Rapid prototyping** | Going from a customer's vague ask to a running prototype in days, not months. |
| **Integration skill** | Wiring an agent into the customer's actual systems (APIs, databases, auth) — this is exactly what **MCP** standardizes. |
| **Evaluation & reliability** | Proving the thing works: evals, traces, guardrails, failure handling. Demos are easy; production is the job. |
| **Customer-facing communication** | Explaining tradeoffs to non-experts, scoping, managing expectations. |
| **Multi-cloud fluency** | Customers are on AWS *or* GCP *or* both. You can't be a one-cloud engineer. (This is why your "both equally" choice is correct.) |

Keep this table open. Every phase below maps back to one or more of these competencies.

---

## 2. The mental model: how the pieces fit together

Before any course, internalize this hierarchy. It's the thing that prevents the "I know 6 tools but can't design a system" trap.

```
                         ┌─────────────────────────────────────┐
                         │            LLM (the brain)           │
                         │   Gemini · Claude · GPT · open-source │
                         └─────────────────────────────────────┘
                                          ▲
              ┌───────────────────────────┼───────────────────────────┐
              │                           │                           │
        ┌───────────┐              ┌──────────────┐            ┌──────────────┐
        │    RAG    │              │    AGENTS    │            │     MCP      │
        │ give the  │              │ let the LLM  │            │ standard plug│
        │ LLM the   │              │ act in loops │            │ for tools &  │
        │ right     │              │ w/ tools,    │            │ data sources │
        │ knowledge │              │ memory, plan │            │ (USB-C for AI)│
        └───────────┘              └──────────────┘            └──────────────┘
              │                           │                           │
              └───────────────┬───────────┴───────────────┬───────────┘
                              ▼                           ▼
                    ┌──────────────────┐        ┌──────────────────┐
                    │   FRAMEWORKS     │        │  MCP SERVERS you  │
                    │ ADK · LangGraph  │        │  build to expose  │
                    │ Strands · CrewAI │        │  tools/data       │
                    └──────────────────┘        └──────────────────┘
                              │
                              ▼
                    ┌────────────────────────────────────────┐
                    │           DEPLOYMENT / RUNTIME           │
                    │  Google: Vertex Agent Engine, Cloud Run  │
                    │  AWS:    Bedrock AgentCore Runtime        │
                    └────────────────────────────────────────┘
```

**Plain-English summary of each concept:**

- **RAG (Retrieval-Augmented Generation):** The LLM doesn't know your private/recent data. RAG retrieves the relevant chunks from your documents and stuffs them into the prompt so the LLM answers grounded in *your* facts.
- **Agents:** Instead of one prompt → one answer, the LLM runs in a loop: *think → pick a tool → observe result → think again* until the task is done. Add **memory** and **planning** and you get autonomous, multi-step behavior.
- **MCP (Model Context Protocol):** A universal standard (think "USB-C for AI") for how an AI app connects to tools and data. Build a tool *once* as an MCP server, and *any* MCP-compatible agent (Claude Desktop, Cursor, your ADK agent, your Bedrock agent) can use it. **Why it matters for FDE:** integration is the bulk of the job, and MCP is now the standard way to do it. It was donated to the **Linux Foundation's Agentic AI Foundation in Dec 2025** (backed by Anthropic, OpenAI, Google, AWS, Microsoft), so it's a *durable, vendor-neutral* skill — not a fad.
- **ADK / LangGraph / Strands:** Frameworks that give you the scaffolding (orchestration, state, tool-calling, multi-agent) so you don't hand-roll the agent loop.
- **Deployment runtimes:** Where the agent actually *runs* in production with scaling, auth, memory, and observability. Google's **Vertex Agent Engine** and AWS's **Bedrock AgentCore** are the two you'll learn.

---

## 3. Prerequisites & environment setup

You have strong Python, so skip Python basics. Set up this toolchain *before* Phase 0.

> **🏠 vs 🏢 strategy:** Your **personal learning stack is local + free**. Your **professional stack is AWS Bedrock** (use your office's account for paid cloud work). Set up the free/local tools fully; only create paid cloud accounts when a phase actually needs them.

**Local dev (free — set up all of these)**
- [ ] **`uv`** — the modern Python package/venv manager (Ed Donner's courses use it; ADK & AgentCore docs recommend it). https://docs.astral.sh/uv/
- [ ] **VS Code** (you already use it) + Python, Jupyter, and an AI coding assistant extension.
- [ ] **Git + a dedicated GitHub repo** for this journey (see [Portfolio strategy](#-portfolio--github-strategy)).
- [ ] **Docker Desktop** — you'll containerize agents in Phase 6/7.

**🏠 Your free local AI stack (this is your default for almost all learning)**
- [ ] ⭐ **Ollama** — run open models (Llama, Qwen, Gemma, Mistral, etc.) locally from the CLI/API. Most course code that calls OpenAI/Anthropic can be pointed at Ollama's OpenAI-compatible endpoint instead, so you learn for **₹0**. https://ollama.com/
- [ ] ⭐ **LM Studio** — a GUI for downloading/running local models with a built-in **OpenAI-compatible local server** and easy model management. Great companion to Ollama; use it to experiment with quantized models and compare them. https://lmstudio.ai/
- [ ] ⭐ **LangChain + LangGraph** — your **core framework** (you named these). LangChain for the building blocks (loaders, retrievers, chains), LangGraph for agent orchestration. Both run fully locally against Ollama/LM Studio. `pip install langchain langgraph` · docs below.
- [ ] **A local vector DB** — **Chroma** (`pip install chromadb`) or **pgvector** in Docker. No cloud needed for RAG learning.

> 💡 **Tip:** Ollama and LM Studio both expose an **OpenAI-compatible API** (`http://localhost:11434/v1` for Ollama, `http://localhost:1234/v1` for LM Studio). In LangChain, point `ChatOpenAI`/`OpenAI` at that `base_url` with a dummy key, and most tutorials "just work" against your free local models.

**☁️ Cloud accounts — create only when the phase needs them**
- [ ] 🏢 ⭐ **AWS Bedrock (professional)** — your production target. *Use your office account/credits where possible.* For solo practice, a personal AWS account works but watch costs; request model access early (Anthropic/Amazon Nova/Meta). https://console.aws.amazon.com/  *(Needed for Phase 6.)*
- [ ] 🆓 **Hugging Face account** (free; needed for the HF courses & model hub from Phase 0). https://huggingface.co/
- [ ] 🆓 **Google AI Studio** (free Gemini API key + generous free tier; for Phase 5 ADK). https://aistudio.google.com/
- [ ] **Google Cloud account** (only for *deploying* ADK in Phase 5; new accounts get free credits). https://console.cloud.google.com/
- [ ] **Anthropic / OpenAI API** (optional — only if you want to run a course exactly as taught instead of via Ollama; small top-ups). https://console.anthropic.com/ · https://platform.openai.com/

**Cost discipline (an FDE skill in itself)**
- **Default to local** (Ollama/LM Studio) for all building and debugging; switch to a hosted model only to verify behavior on a frontier model or when a feature needs it.
- For paid cloud, **prefer the office's AWS account** for Bedrock work; keep personal spend near zero.
- Use the cheapest capable hosted model when you do go cloud (e.g., `amazon nova-lite`/`claude-haiku` on Bedrock, `gemini-2.5-flash` on Google).
- Set **billing alerts** on any cloud account *the day you create it*.

---

## 4. The roadmap at a glance

| Phase | Focus | Primary resource | Est. effort | FDE competency |
|---|---|---|---|---|
| **0** | ML/LLM foundations | Free (Karpathy, 3B1B, HF) | 15–25 h | Architectural judgment |
| **1** | LLM Engineering Core | ⭐ *Your Course #1* (Ed Donner Core) | 40–60 h | Prototyping |
| **2** | RAG mastery (deep) | DeepLearning.AI + LlamaIndex/LangChain docs | 25–40 h | Architecture, eval |
| **3** | Agents: patterns & frameworks | ⭐ *Your Course #2* + HF Agents Course | 40–60 h | Architecture, prototyping |
| **4** | MCP servers & clients | ⭐ Anthropic free courses + Eden Marco | 20–30 h | **Integration** |
| **5** | Google ADK | ⭐ Official ADK docs + Google Skills | 25–40 h | Frameworks, GCP |
| **6** | AWS Bedrock & AgentCore | ⭐ AWS docs + workshops | 25–40 h | AWS, deployment |
| **7** | Production: deploy/observe/eval/secure | ⭐ *Your Course #3* (Ed Donner Production) | 30–50 h | Reliability |
| **8** | Capstone & FDE readiness | Self-directed build | 40–80 h | Everything |

**Total:** ~260–425 focused hours. At a relaxed ~10 h/week that's roughly 6–10 months; faster if you go heavier. The capstone is where it all consolidates — don't rush to it, but don't skip it.

> **💸 Free-first execution:** Phases 0–5 can be done **almost entirely for free, locally** — Ollama/LM Studio for models, LangChain/LangGraph as your framework, Chroma/pgvector for RAG, and free official docs/courses. The only phase that *requires* spend is **Phase 6 (AWS Bedrock)** — and that's your **professional environment**, so lean on your office's AWS account there. Treat paid personal API keys as optional "verify on a frontier model" top-ups, not a default.

> **Your framework choice:** Since you've named **LangChain + LangGraph**, that's your **home framework** for Phases 2–4 and 7. You'll still *meet* ADK (Phase 5) and Strands (Phase 6), but you build deepest in LangGraph. Bonus: LangGraph is the most in-demand agent framework in production job listings, and it runs against Bedrock *and* local models, so it spans both your worlds.

> **Note on your three courses:** They're the spine of this plan and they're well-chosen (Ed Donner / Ligency, refreshed for 2026, strongly rated). Phases 2, 4, 5, 6 are the *additions* that turn "I finished some courses" into "I can architect and ship GenAI systems for work (AWS) and prototype anything locally (free)." Your Course #2 ("Agentic Track") already includes an MCP section — Phase 4 deepens it into real server-building skill.

---

## Phase 0 — ML/LLM foundations (no black boxes)

**Goal:** Understand *why* LLMs work well enough that nothing later is magic. You don't need the math to build, but FDEs who understand tokens, embeddings, context windows, and attention make far better architecture calls. Keep this light and conceptual — resist the urge to go down a deep-learning rabbit hole.

**Do this (pick what resonates, ~15–25 h):**
- 🆓 ⭐ **3Blue1Brown — Neural Networks series** (esp. the "But what is a GPT?" / Transformers & Attention videos). Best intuition-builder anywhere: https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi
- 🆓 ⭐ **Andrej Karpathy — "Let's build GPT from scratch"** (and his *Neural Networks: Zero to Hero* series). You build a tiny GPT in code — demystifies everything: https://www.youtube.com/watch?v=kCc8FmEb1nY
- 🆓 **Jay Alammar — The Illustrated Transformer** (the classic visual explainer): https://jalammar.github.io/illustrated-transformer/
- 🆓 **Hugging Face LLM Course** (Transformers, tokenization, embeddings — hands-on): https://huggingface.co/learn/llm-course
- 🆓 **Anthropic — Prompt Engineering** interactive tutorial & docs (prompting is your highest-leverage skill): https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview

**Key concepts to be able to explain out loud (your checkpoint):**
- [ ] Token, context window, temperature, top-p
- [ ] Embeddings & vector similarity (cosine) — *the* foundation of RAG
- [ ] What attention does, conceptually
- [ ] Pretraining vs fine-tuning vs in-context learning (RAG/prompting)
- [ ] Why hallucination happens and what reduces it (grounding, retrieval, evals)

**✅ Definition of Done:** You can explain to a non-technical colleague why an LLM "knows" some things and not others, and why RAG vs fine-tuning solves different problems.

---

## Phase 1 — LLM Engineering Core

**Goal:** Become fluent building real LLM apps end-to-end. This is **your Course #1** and it's the perfect spine — it covers Frontier + open-source models, Hugging Face, LangChain, Gradio, RAG, QLoRA fine-tuning, and an autonomous multi-agent capstone, all project-based.

**Primary (⭐ do all 8 projects):**
- 💰 ⭐ **AI Engineer Core Track: LLM Engineering, RAG, QLoRA, Agents** (Ed Donner): https://www.udemy.com/course/llm-engineering-master-ai-and-large-language-models/
- 🆓 **Course resources / slides hub** (bookmark this): https://edwarddonner.com/2024/11/13/llm-engineering-resources/
- 🆓 **Course code repo** (follow along, commit your variations): https://github.com/ed-donner/llm_engineering

**How to do it well (FDE mindset + free-first):**
- Don't just copy the notebooks. After each project, **rebuild one feature from scratch** without looking.
- ⭐ **Run as much as possible on Ollama/LM Studio.** The course calls hosted APIs; for most projects you can swap in a local model via the OpenAI-compatible endpoint and learn for free. Use a paid API only where the project specifically needs a frontier model (e.g., the code-optimization or fine-tuning projects).
- **Practice the swap both ways:** one project on a local model, the same project pointed at **Bedrock** (your work cloud) so you see the exact same LangChain code run in both worlds.
- Push every project to your GitHub journey repo with a short README explaining the architecture.

**Supplementary (optional, 🆓):**
- **DeepLearning.AI — short courses** (1–2 h each, excellent): *ChatGPT Prompt Engineering for Developers*, *Building Systems with the ChatGPT API*, *LangChain for LLM Application Development*: https://www.deeplearning.ai/courses/

**✅ Definition of Done:** You've shipped all 8 course projects, run at least one fully on a **local model (Ollama/LM Studio)** and one on **Bedrock**, and can build a basic RAG chatbot from a blank file without a tutorial.

---

## Phase 2 — RAG mastery (deep)

**Goal:** Go *beyond* "RAG works in the demo" to "I can design and debug RAG that's accurate in production." RAG quality is where most real GenAI projects live or die, so this is disproportionately valuable for an FDE. Course #1 introduces RAG; this phase makes you genuinely good at it.

**Core concepts to master:**
| Topic | Why it matters |
|---|---|
| **Chunking strategies** (fixed, recursive, semantic, parent-document) | Bad chunking = bad retrieval, no matter how good the model. |
| **Embedding models** (choosing, dimensions, domain fit) | The retrieval quality ceiling. |
| **Vector databases** (pgvector, Chroma, Qdrant, Pinecone, Weaviate; cloud-native: Vertex Vector Search, Bedrock Knowledge Bases) | You'll be asked to pick one per customer. |
| **Retrieval strategies** (dense, sparse/BM25, **hybrid**, MMR) | Hybrid usually wins; know when. |
| **Reranking** (cross-encoders, Cohere/Voyage rerankers) | Biggest easy accuracy win. |
| **Query transformation** (HyDE, multi-query, decomposition) | Handles vague/complex questions. |
| **Evaluation** (RAGAS: faithfulness, answer/context relevancy) | *You cannot improve what you don't measure.* FDE-critical. |
| **Advanced RAG** (agentic RAG, GraphRAG, contextual retrieval) | The 2026 frontier. |

**Do this:**
- 🆓 ⭐ **DeepLearning.AI — Advanced Retrieval for AI with Chroma**: https://www.deeplearning.ai/short-courses/
- 🆓 ⭐ **DeepLearning.AI — Building and Evaluating Advanced RAG** (RAGAS + LlamaIndex): https://www.deeplearning.ai/short-courses/
- 🆓 **DeepLearning.AI — Knowledge Graphs for RAG** (Neo4j) — for GraphRAG: https://www.deeplearning.ai/short-courses/
- 🆓 ⭐ **LlamaIndex docs** (the RAG-first framework — read the "Understanding" + "Optimizing" sections): https://docs.llamaindex.ai/
- 🆓 **LangChain RAG docs/tutorials**: https://python.langchain.com/docs/tutorials/rag/
- 🆓 ⭐ **RAGAS evaluation framework** (learn to score your RAG): https://docs.ragas.io/
- 🆓 **Anthropic — Contextual Retrieval** (a high-impact 2024/25 technique): https://www.anthropic.com/news/contextual-retrieval

**🛠 Project (do this — it's portfolio gold):**
Build a **"Chat with my documents" RAG service** over a real corpus (e.g., a set of PDFs relevant to your domain), **entirely locally and free** — LangChain + a local embedding model + **Chroma/pgvector** + a model served by **Ollama/LM Studio**. Requirements:
1. Two chunking strategies, compared.
2. Hybrid retrieval + a reranker.
3. A **RAGAS evaluation harness** with a small labeled question set, reporting faithfulness & relevancy before/after your improvements.
4. A Gradio or simple FastAPI front end.
5. *(Stretch, for the work track)* Re-point the same pipeline at **Amazon Bedrock** models + a **Bedrock Knowledge Base** and compare quality/cost vs your local build (you'll formalize this in Phase 6).

> 💡 *Domain tie-in:* If you build this over de-identified medical/clinical reference material, it doubles as a prototype for a privacy-aware medical-knowledge assistant — directly relevant to patient-records work. Keep all data synthetic/de-identified for learning.

**✅ Definition of Done:** You can take a RAG pipeline that's giving wrong answers and systematically diagnose whether the problem is chunking, retrieval, reranking, or generation — and prove the fix with RAGAS numbers.

---

## Phase 3 — Agents: patterns & frameworks

**Goal:** Understand agent **design patterns** first (these transfer across every framework), then get hands-on with frameworks. This is **your Course #2** plus the free HF course for breadth.

**The four patterns to internalize (they recur everywhere — ADK, LangGraph, AgentCore all implement these):**
1. **Reflection** — the agent critiques and improves its own output.
2. **Tool Use** — the agent calls functions/APIs to act.
3. **Planning** — the agent decomposes a goal into steps.
4. **Multi-Agent** — specialized agents collaborate/delegate (a "manager" routing to "workers").

**Primary:**
- 💰 ⭐ **AI Engineer Agentic Track: The Complete Agent & MCP Course** (Ed Donner — your Course #2). Covers agent frameworks + an MCP intro that Phase 4 builds on.
- 🆓 ⭐ **Hugging Face Agents Course** (free, certified; teaches **smolagents, LlamaIndex, LangGraph** + agentic RAG; ~3–4 h/unit). Excellent because it separates *concepts* from *framework syntax*: https://huggingface.co/learn/agents-course/en/unit0/introduction
- 🆓 **DeepLearning.AI — *Agentic AI* (Andrew Ng)** — the canonical "four design patterns" course; framework-agnostic: https://www.deeplearning.ai/courses/

**⭐ Your home framework: LangChain + LangGraph (committed).** Go deep here — this is the framework you build in for the rest of the plan, it runs against both **local models (Ollama/LM Studio)** and **Bedrock**, and it's the most in-demand agent framework in production job listings.
- 🆓 ⭐ **LangGraph docs** (start with the quickstart + "agentic concepts" + persistence/memory): https://langchain-ai.github.io/langgraph/
- 🆓 ⭐ **LangChain Academy — *Introduction to LangGraph*** (free, official, hands-on): https://academy.langchain.com/
- 🆓 **DeepLearning.AI — *AI Agents in LangGraph*** (free short course): https://www.deeplearning.ai/courses/
- 🆓 **LangChain RAG + tool/agent docs** (your building blocks): https://python.langchain.com/docs/

> You'll still *meet* smolagents/LlamaIndex (in the HF course) and ADK/Strands (Phases 5–6), but treat those as "read the docs, build one thing." LangGraph is where you develop real depth.

**🛠 Project:** Build a **multi-agent system in LangGraph, running on a local model (Ollama/LM Studio) — free** — e.g., a *research assistant* with a planner node, a web-search/tool node, and a writer node that produces a sourced report. Use LangGraph **checkpointers for memory** across turns. Include at least one **custom tool**. (You'll later redeploy this exact system to Bedrock AgentCore in Phase 6.)

**✅ Definition of Done:** You can explain Reflection/Tool-Use/Planning/Multi-Agent with a real example of each, and you've shipped a working multi-agent app with custom tools and memory.

---

## Phase 4 — MCP: build servers & clients

**Goal:** Make MCP a *strength*. For an FDE this is arguably the highest-ROI skill in the whole plan — it's how you'll integrate agents into each customer's tools and data, and it's now an industry standard (10,000+ public servers, ~97M monthly SDK downloads as of late 2025). You'll build both **servers** (expose tools/data) and **clients** (consume them).

**Concepts to master:**
- The three **primitives**: **Tools** (model-controlled actions), **Resources** (app-controlled data at a URI), **Prompts** (user-controlled templates) — and when to use each.
- **Transports**: `stdio` (local) vs **Streamable HTTP/SSE** (remote/scalable).
- **JSON-RPC 2.0** message flow; capability discovery (`tools/list`).
- **MCP Inspector** for debugging (`npx @modelcontextprotocol/inspector`).
- Security & auth for remote servers (a production must).

**Primary (⭐ free official first):**
- 🆓 ⭐ **MCP official site & spec** (the canonical source): https://modelcontextprotocol.io/
- 🆓 ⭐ **Anthropic — Introduction to MCP** (build servers & clients in Python): https://anthropic.skilljar.com/introduction-to-model-context-protocol
- 🆓 ⭐ **Anthropic — MCP: Advanced Topics** (sampling, notifications, transports, production scaling): https://anthropic.skilljar.com/model-context-protocol-advanced-topics
- 🆓 **Hugging Face MCP Course** (vendor-neutral, Python + TypeScript, partnered with Anthropic): https://huggingface.co/learn/mcp-course
- 💰 **Eden Marco — MCP Crash Course** (Udemy; thorough server/client/tools/resources/security, ~8.5 h): https://www.udemy.com/course/model-context-protocol/

**Reference:**
- 🆓 **MCP Python SDK / FastMCP** (what you'll actually code with): https://github.com/modelcontextprotocol/python-sdk
- 🆓 **Official servers (read real code)**: https://github.com/modelcontextprotocol/servers

**🛠 Project (high portfolio value):** Build a **custom MCP server** that wraps a real API or database you care about (e.g., a WordPress/WhatsApp integration, a Postgres database, or a domain API). Expose 3–4 tools + 1 resource. Then:
1. Debug it with **MCP Inspector**.
2. Connect it to **Claude Desktop** and to your Phase-3 agent.
3. Deploy the HTTP version somewhere (Cloud Run or behind AgentCore Gateway in Phase 6).

> 💡 *Domain tie-in:* An MCP server exposing consent-gated access to (synthetic) patient records — `get_record(patient_id)`, `list_consents`, `request_access` — is a near-perfect FDE demo *and* a prototype for your records platform's agent layer.

**✅ Definition of Done:** You've built, debugged, and connected a custom MCP server to at least two different hosts, and you can explain Tools vs Resources vs Prompts and stdio vs HTTP transport without notes.

---

## Phase 5 — Google ADK (Agent Development Kit)

**Goal:** Learn Google's open-source, code-first agent framework — your **breadth play** for the second cloud and a strong portfolio differentiator. It's largely **free to learn**: build locally and use Gemini's generous free tier (Google AI Studio) plus new-account Cloud credits for the one deployment exercise. ADK is what powers Google's own products (Agentspace, CES), is **model-agnostic** (Gemini natively; others via LiteLLM — so you can even point it at local models), and **deployment-agnostic**.

> **Where this fits your two-environment plan:** Bedrock (Phase 6) is your *work* cloud, so prioritize it. ADK here makes you genuinely **multi-cloud** — which is a real FDE edge — without much spend. If your time is tight, you can do Phase 6 before Phase 5; just don't skip ADK entirely, since "I've shipped agents on both Google and AWS" is a standout line.

> **Current state (June 2026):** ADK is at **2.0**, Python **3.10+**, built on two core classes — **`Agent`** (instructions, tools, behavior) and **`Workflow`** (graph-based orchestration: routing, fan-out/fan-in, loops, retries, human-in-the-loop). Bi-weekly release cadence, so always check the docs version. Note ADK 2.0 introduced breaking changes vs older 1.x.

**Primary (⭐ official):**
- 🆓 ⭐ **ADK Documentation** (start here — quickstart, core concepts, multi-agent, tools, eval): https://google.github.io/adk-docs/
- 🆓 ⭐ **ADK Python repo** (samples in `contributing/` are gold): https://github.com/google/adk-python
- 🆓 **Google Skills — "Get Started with ADK"** (hands-on lab, free): https://www.skills.google/focuses/125064
- 🆓 **Google Cloud — Build & deploy an ADK agent (quickstart)**: https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents/quickstart-adk
- 🆓 **Google Developers Blog — ADK intro** (the "why" + multi-agent walkthrough): https://developers.googleblog.com/en/agent-development-kit-easy-to-build-multi-agent-applications/

**What to build through (in order):**
1. **Single agent** with a custom Python-function tool (ADK reads your docstring to know when to call it).
2. **Multi-agent hierarchy** — a coordinator that delegates to specialist sub-agents.
3. **Workflow agent** — deterministic graph with routing + a loop + human-in-the-loop.
4. **Add an MCP tool** to an ADK agent (connects Phase 4 → Phase 5).
5. **Use the `adk web` UI** to inspect execution step-by-step, and write an **eval set** to score the agent.
6. **Deploy** to **Vertex Agent Engine** (managed) and/or **Cloud Run** (`AdkApp` + the Agent Engine SDK).

**🛠 Project:** Rebuild your Phase-3 multi-agent research assistant **in ADK**, deployed to Cloud Run or Agent Engine, using Gemini, with at least one MCP tool and an eval set. Comparing the same system across two frameworks is exactly the kind of judgment FDE interviews probe.

**✅ Definition of Done:** You've deployed a multi-agent ADK system to Google Cloud, it uses Gemini + at least one MCP tool, and you've evaluated it with an ADK eval set.

---

## Phase 6 — AWS Bedrock & AgentCore

**Goal:** ⭐ **This is your professional environment — treat it as the priority track.** You'll deploy your **LangGraph** agents and RAG to AWS the way you'll do it at work. AWS's agent story now centers on **Amazon Bedrock AgentCore**: a framework-agnostic, model-agnostic platform for *running* agents in production. Good news — **AgentCore explicitly supports LangGraph**, so your home-framework code deploys here directly.

> **💸 Cost note:** This is the one phase that needs real cloud spend. **Use your office's AWS account/credits** wherever your role allows it — that's the whole point of the two-environment split. For solo practice outside work, scale-to-zero Runtime + cheap models (Amazon Nova-lite, Claude Haiku) keep costs low; set a billing alarm before you start and tear down resources after each session.

> **Current state (June 2026):** **AgentCore** is GA and modular — use pieces independently:
> - **Runtime** — serverless, session-isolated agent hosting (sessions up to 8h, scale-to-zero).
> - **Memory** — short-term (multi-turn) + long-term (cross-session) with automatic embeddings/retrieval.
> - **Gateway** — turns APIs, Lambda functions, and **MCP servers** into agent-ready tools (semantic tool search included).
> - **Identity** — OAuth token vault, API-key management (integrates Cognito/Okta/Entra).
> - **Code Interpreter / Browser** — sandboxed code execution & web interaction.
> - **Observability** — OpenTelemetry-based tracing/dashboards via CloudWatch.
> It works with **Strands Agents** (AWS's open-source framework, recommended by AWS), **LangGraph (your framework), CrewAI, LlamaIndex, Google ADK, and OpenAI Agents SDK**. The **AgentCore CLI (`@aws/agentcore`)** is the recommended way to build/deploy.

**Foundations first (Bedrock itself):**
- 🆓 ⭐ **Amazon Bedrock User Guide** — models, **Knowledge Bases** (managed RAG!), Guardrails, prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/
- 🆓 **Bedrock simple agent tutorial** (console → Lambda tool → invoke from Python/boto3): https://docs.aws.amazon.com/bedrock/latest/userguide/agent-tutorial.html
- 🆓 ⭐ **AWS Workshop Studio — search "Bedrock" / "AgentCore"** for free guided labs: https://workshops.aws/

**AgentCore (⭐ official):**
- 🆓 ⭐ **AgentCore Developer Guide** (overview + concepts): https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- 🆓 ⭐ **AgentCore CLI quickstart** (zero → deployed agent): https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-get-started-cli.html
- 🆓 **AgentCore Starter Toolkit & samples**: https://aws.github.io/bedrock-agentcore-starter-toolkit/
- 🆓 **Strands Agents** (AWS's open agent framework): https://strandsagents.com/

**What to build through:**
1. **Bedrock Knowledge Base** — a managed RAG system (compare it to your hand-built local Phase-2 RAG; understand the build-vs-buy tradeoff — a core FDE conversation).
2. ⭐ **Deploy your Phase-3 LangGraph agent to AgentCore Runtime** via the CLI (this is the payoff of choosing LangGraph as your home framework — same code, now production). Optionally also try **Strands Agents** (AWS's own framework, https://strandsagents.com/) once, just to compare.
3. Add **AgentCore Memory** and an **AgentCore Gateway** that exposes your **Phase-4 MCP server** as tools.
4. Wire up **Observability** and inspect a trace.

**🛠 Project:** Deploy your **LangGraph** research-assistant agent to **AgentCore Runtime**, backed by a **Bedrock Knowledge Base** for RAG, **AgentCore Memory** for state, and your **MCP server via Gateway**. Combined with the Phase-5 ADK deploy, you now have *the same conceptual system running on both clouds, plus locally* — the centerpiece of a multi-cloud FDE portfolio.

> ⚠️ FDE reality check: AWS IAM/permissions setup is genuinely fiddly. Budget extra time, and treat "I made IAM + Bedrock model access work" as a real skill — customers struggle with exactly this.

**✅ Definition of Done:** You've deployed an agent on AgentCore with Memory + a Gateway-exposed MCP server + a Bedrock Knowledge Base, and you can articulate when to use managed (Knowledge Bases/AgentCore) vs DIY components.

---

## Phase 7 — Production: deploy, observe, evaluate, secure

**Goal:** Turn "it works on my machine" into "it works reliably for a customer." This is **your Course #3** plus the cross-cutting production skills that separate engineers from demo-makers — and it's the FDE differentiator.

**Primary:**
- 💰 ⭐ **AI Engineer Production Track: Deploy LLMs & Agents at Scale** (Ed Donner — your Course #3; scaling, pipelines, monitoring, enterprise rollout incl. AWS).

**Cross-cutting production topics (build these into your capstone):**
| Topic | Tools / resources |
|---|---|
| **Observability & tracing** | 🆓 **Langfuse** (open-source, self-hostable): https://langfuse.com/docs · **LangSmith**: https://docs.smith.langchain.com/ · OpenTelemetry (native in ADK & AgentCore). |
| **Evaluation (systematic)** | RAGAS (RAG), ADK eval sets, AgentCore evaluators, **DeepEval**: https://docs.confident-ai.com/ |
| **Guardrails & safety** | **Bedrock Guardrails**; **Gemini safety settings**; input/output validation; PII redaction. |
| **Prompt/cost management** | Caching, model routing (cheap model first), token budgeting, **LiteLLM** for multi-provider: https://docs.litellm.ai/ |
| **Security** | Prompt-injection defense, secrets management, least-privilege IAM, tool-call authorization (AgentCore Identity). You already do security work on drprettypsy.com — this extends that instinct to AI. |
| **Serving & scale** | FastAPI + containers; Cloud Run / AgentCore Runtime; streaming responses; concurrency. |
| **CI/CD** | GitHub Actions to test + deploy your agents; eval-gated deploys (don't ship if eval scores drop). |

**🆓 Read for the production mindset:**
- **Anthropic — "Building effective agents"** (the definitive practitioner essay; read it twice): https://www.anthropic.com/engineering/building-effective-agents
- **Google — Agent design patterns & best practices** (in ADK docs).

**🛠 Project:** Take *one* of your earlier agents and make it **production-grade**: tracing on every call, an eval suite that runs in CI, guardrails, a guardrailed system prompt, cost logging, and a containerized deploy with a health check. Write a short "runbook" README (what to do when it breaks) — FDEs live in runbooks.

**✅ Definition of Done:** One of your agents has tracing, CI-gated evals, guardrails, and a documented deploy + runbook. You can answer "how do you know it works?" with metrics, not vibes.

---

## Phase 8 — Capstone & FDE readiness

**Goal:** Build one ambitious, end-to-end, *integrated* system that exercises everything — and package it so it sells you in interviews.

**Capstone requirements (hit all of these):**
- [ ] **RAG** over a real document corpus, with evaluation.
- [ ] **Multi-agent** orchestration (planner + specialists).
- [ ] At least one **custom MCP server** you built, consumed by the agent.
- [ ] Deployed on **at least one cloud** (bonus: demonstrate it on both ADK/Vertex *and* AgentCore).
- [ ] **Observability + evals + guardrails** wired in.
- [ ] A clean **README + architecture diagram + short demo video (Loom)**.

**Capstone ideas (pick one that you'd actually use):**
1. ⭐ **Consent-gated medical knowledge agent** — patients/clinicians query (synthetic, de-identified) records; an MCP server enforces time-limited, revocable access; agentic RAG answers grounded questions with citations; guardrails block PII leakage. *Directly aligned with your patient-records platform and a standout FDE demo.* (Keep all data synthetic; treat real regulatory work, e.g., DPDP Act / ABDM, as design notes, not live data.)
2. **Internal "company expert" assistant** — RAG over a company's docs + agents that take actions via MCP-wrapped internal APIs (the classic FDE deliverable).
3. **Investment research agent** — multi-agent system that pulls market data via tools, runs RAG over filings, and produces a sourced thesis. (Leans into your equities interest; keep it educational, not advice.)

**FDE-specific prep (in parallel with the capstone):**
- **Practice the "scope a solution live" muscle:** take a vague problem ("our support team is drowning in tickets") and, in 30 minutes, sketch an architecture, name the tradeoffs, and identify the riskiest assumption. Do this weekly.
- **Communication reps:** write a 1-page "solution proposal" for each capstone feature, as if for a non-technical client.
- **Read job descriptions** for FDE / Forward Deployed AI Engineer roles (Anthropic, Palantir, OpenAI, scale-ups) and reverse-engineer the skills they list into gaps to close.
- **Mock the integration question:** be ready to whiteboard "how would you connect this agent to the customer's Salesforce/EHR/database?" — the answer increasingly starts with "an MCP server."

**✅ Definition of Done:** A polished, deployed, multi-component capstone on GitHub with a demo video, *and* you can confidently walk an interviewer through your architecture and defend every tradeoff.

---

## ✅ FDE competency checklist

Tick these off as you go — this is your "am I ready?" scorecard.

**Build**
- [ ] Build a RAG pipeline from scratch and improve its RAGAS scores measurably
- [ ] Choose chunking/embedding/retrieval/reranking appropriately and justify it
- [ ] Explain & implement the 4 agent patterns (Reflection, Tool Use, Planning, Multi-Agent)
- [ ] Build a multi-agent system in **two** frameworks (e.g., LangGraph + ADK)
- [ ] Build, debug, and deploy a **custom MCP server**; consume it from multiple hosts
- [ ] Build & fine-tune with QLoRA at least once (you'll do this in Course #1)

**Deploy (multi-cloud)**
- [ ] Deploy an agent on **Google** (Vertex Agent Engine / Cloud Run via ADK)
- [ ] Deploy an agent on **AWS** (Bedrock AgentCore Runtime)
- [ ] Stand up managed RAG (Bedrock Knowledge Base) *and* explain build-vs-buy

**Operate**
- [ ] Add tracing/observability (Langfuse/LangSmith/OTel) to an agent
- [ ] Write an eval suite and gate deploys on it (CI)
- [ ] Add guardrails + PII handling + least-privilege auth
- [ ] Write a runbook for an agent in production

**Communicate**
- [ ] Scope a fuzzy customer problem into an architecture in <30 min
- [ ] Explain RAG/agents/MCP to a non-technical stakeholder
- [ ] Defend a tech-choice tradeoff (cost vs latency vs accuracy)

---

## 📦 Portfolio & GitHub strategy

Your portfolio *is* your FDE résumé. Do this from Phase 1, not at the end.

- **One "journey" repo** with a folder per phase, each containing the project + a README (problem, architecture, what you learned, screenshots).
- **3–4 "flagship" repos** broken out separately and polished: your **MCP server**, your **multi-cloud agent**, and your **capstone**.
- Every flagship repo gets: a **clear README**, an **architecture diagram** (draw.io / Excalidraw / Mermaid), setup instructions, and a **Loom/YouTube demo (2–4 min)**.
- **Write as you learn.** A short blog post or LinkedIn write-up per phase ("I built an MCP server that does X — here's what I learned") compounds enormously for FDE roles, which value communication. You already maintain a site (drprettypsy.com) — you have the muscle.
- **Pin** your flagship repos on your GitHub profile.

---

## 🔄 Staying current

GenAI moves fast (ADK ships bi-weekly; AgentCore monthly). Build a light habit:
- 🆓 **Anthropic Engineering blog**: https://www.anthropic.com/engineering · **Google Developers Blog (AI)** · **AWS ML/Bedrock blog**
- 🆓 **AgentCore release notes** (so your AWS knowledge doesn't go stale): https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html
- 🆓 **DeepLearning.AI "The Batch"** newsletter (best signal-to-noise weekly): https://www.deeplearning.ai/the-batch/
- 🆓 **Latent Space** podcast/newsletter (engineer-focused) · **Hugging Face Daily Papers** for the frontier.
- Re-skim the **ADK** and **AgentCore** docs every couple of months — they change.

---

## 📚 Quick-reference link library

**Your three core courses (the spine)**
- Core: https://www.udemy.com/course/llm-engineering-master-ai-and-large-language-models/
- Course resources hub: https://edwarddonner.com/2024/11/13/llm-engineering-resources/
- Code: https://github.com/ed-donner/llm_engineering

**🏠 Your free local stack** — Ollama (https://ollama.com/) · LM Studio (https://lmstudio.ai/) · LangChain docs (https://python.langchain.com/docs/) · LangGraph docs (https://langchain-ai.github.io/langgraph/) · LangChain Academy (https://academy.langchain.com/) · Chroma (https://docs.trychroma.com/)

**Foundations** — 3Blue1Brown · Karpathy (https://www.youtube.com/watch?v=kCc8FmEb1nY) · Illustrated Transformer (https://jalammar.github.io/illustrated-transformer/) · HF LLM Course (https://huggingface.co/learn/llm-course)

**RAG** — LlamaIndex (https://docs.llamaindex.ai/) · LangChain RAG (https://python.langchain.com/docs/tutorials/rag/) · RAGAS (https://docs.ragas.io/) · Contextual Retrieval (https://www.anthropic.com/news/contextual-retrieval)

**Agents** — ⭐ LangGraph (https://langchain-ai.github.io/langgraph/) · LangChain Academy (https://academy.langchain.com/) · HF Agents Course (https://huggingface.co/learn/agents-course/en/unit0/introduction) · Building Effective Agents (https://www.anthropic.com/engineering/building-effective-agents)

**MCP** — Official (https://modelcontextprotocol.io/) · Anthropic Intro (https://anthropic.skilljar.com/introduction-to-model-context-protocol) · Anthropic Advanced (https://anthropic.skilljar.com/model-context-protocol-advanced-topics) · HF MCP Course (https://huggingface.co/learn/mcp-course) · Python SDK (https://github.com/modelcontextprotocol/python-sdk) · Eden Marco (https://www.udemy.com/course/model-context-protocol/)

**Google ADK** — Docs (https://google.github.io/adk-docs/) · Python (https://github.com/google/adk-python) · Google Skills lab (https://www.skills.google/focuses/125064) · Cloud quickstart (https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents/quickstart-adk)

**AWS Bedrock / AgentCore (🏢 your work cloud)** — Bedrock guide (https://docs.aws.amazon.com/bedrock/latest/userguide/) · AgentCore guide (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) · AgentCore CLI quickstart (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-get-started-cli.html) · Starter toolkit (https://aws.github.io/bedrock-agentcore-starter-toolkit/) · Strands (https://strandsagents.com/) · Workshops (https://workshops.aws/)

**Production** — Langfuse (https://langfuse.com/docs) · LangSmith (https://docs.smith.langchain.com/) · DeepEval (https://docs.confident-ai.com/) · LiteLLM (https://docs.litellm.ai/)

**Tooling** — uv (https://docs.astral.sh/uv/) · Docker (https://www.docker.com/) · Google AI Studio (https://aistudio.google.com/)

---

*Built for a project-first path to Forward Deployed Engineer: **free & local for personal learning (Ollama/LM Studio + LangChain/LangGraph), AWS Bedrock for the professional track**. Keep the rule: understand the pattern before you learn the framework, build locally for free wherever you can, and ship something at the end of every phase.*