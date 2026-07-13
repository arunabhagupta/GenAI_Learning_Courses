# ⚡ FDE Crash Course — 4 Weeks / ~60 Hours

> A ruthless compression of `GenAI_Learning_Path.md` for **15 hrs/week × 4 weeks**, starting from "Phase 0–1 in progress."
>
> **The honest deal:** the full roadmap is 260–425 hours. Sixty hours cannot make you expert at everything in it. What this plan *can* do — and does — is get you to **FDE-core competency**: you can build production-pattern RAG, orchestrate agents in LangGraph, write a custom MCP server, deploy to Bedrock AgentCore, and defend every choice in an interview. Everything else moves to the [Month-2 backlog](#-month-2-backlog-what-we-deferred).
>
> **Last updated:** July 2026 · Companion to the full roadmap — don't delete that file, you'll return to it.

---

## 🎯 The One Rule That Makes This Work

**You build ONE system, layer by layer, all month.** No throwaway exercises. Every week's output is a layer of your capstone:

```
Week 1 → skills + skeleton     (LLM calls, prompting, local stack running)
Week 2 → the RAG layer          (ingestion, retrieval, reranking, RAGAS evals)
Week 3 → the agent + MCP layer  (LangGraph orchestration, custom MCP server)
Week 4 → the production layer   (Bedrock/AgentCore deploy, guardrails, tracing, README)
```

By day 28 you have one deployed, evaluated, multi-agent, MCP-integrated system on AWS — which is worth more in an FDE interview than eight tutorial projects.

---

## 🏗 Pick Your Capstone (Day 1 decision — don't overthink it)

Both hit every FDE competency. Pick the one you'll finish.

### Option A (recommended): **BookingPing Support Agent**
An AI assistant for WordPress booking-plugin users.
- **RAG layer:** ingest docs for Amelia/Bookly/LatePoint/BookingPress + WhatsApp Cloud API docs + your own BookingPing docs → answers setup/troubleshooting questions with citations.
- **Agent layer (LangGraph):** router → RAG-answerer / troubleshooter / escalation nodes.
- **MCP server:** wraps APIs you *already know* — e.g., `send_whatsapp_template`, `check_booking_status`, `list_templates` against Meta's Graph API (sandbox/test number).
- **Why A:** you already know the domain and the APIs cold, so zero hours are lost learning the problem space — and it doubles as real groundwork for your actual product.

### Option B: **Consent-Gated Medical Knowledge Agent**
The roadmap's flagship idea: agentic RAG over synthetic clinical reference docs, with an MCP server enforcing time-limited record access (`get_record`, `list_consents`, `request_access`). Stronger "wow" demo; costs ~3–4 extra hours building synthetic data and consent logic. All data synthetic/de-identified.

**Capstone requirements (both options):**
- [ ] RAG with hybrid retrieval + reranking, scored with RAGAS (before/after numbers)
- [ ] Multi-agent LangGraph orchestration with memory (checkpointer)
- [ ] One custom MCP server (3+ tools), consumed by the agent AND Claude Desktop
- [ ] Deployed on **Bedrock AgentCore Runtime**, RAG optionally via **Bedrock Knowledge Base**
- [ ] Guardrails + tracing (Langfuse or LangSmith)
- [ ] README + architecture diagram (Mermaid/Excalidraw) + 3-min Loom demo

---

## 📏 Ground Rules (this is how 60h beats 400h)

1. **Timebox hard.** Every session below has a scope. When time's up, ship what you have and move on. Perfectionism is the enemy of the month.
2. **Videos at 1.75–2×, code at 1×.** Watch to orient; learn by building. If you can already do what a video teaches, skip it.
3. **Ollama/LM Studio for everything** until Week 4. Point `ChatOpenAI` at `http://localhost:11434/v1`. Zero API spend until Bedrock week (use the office account there).
4. **Ed Donner Core = reference library, not a serial watch.** You don't have 40–60h for it. Use the sections mapped below; skip projects that duplicate your capstone layers. (You keep the course — finish the rest in month 2.)
5. **Commit daily** to your journey repo. The README you write on day 28 is built from these commits.
6. **Weekday sessions = 2h, weekend sessions = 2.5h.** 5 weekday + 2 weekend = 15h/week. If you miss a session, steal from the weekend — never from Week 4.

---

## 📅 WEEK 1 — Foundations Sprint + LLM Engineering Core (15h)

**Goal:** close out Phase 0 fast, get fluent with the local stack, and stand up the capstone skeleton. Since you're mid-Phase-0/1, skip anything you've already done and bank the time.

| Session | Hours | Do this |
|---|---|---|
| **Mon** | 2h | **Phase 0 closeout.** 3Blue1Brown "But what is a GPT?" + Attention video (2× speed). Skim The Illustrated Transformer. Then write, in your own words in the repo README, answers to the 5 checkpoint concepts (token/context window, embeddings + cosine similarity, attention, pretraining vs fine-tuning vs RAG, why hallucination happens). **Skip Karpathy's build-from-scratch** — it's brilliant but it's 4+ hours; deferred. |
| **Tue** | 2h | **Local stack.** `uv` project + Git repo. Ollama pulling 2 models (e.g., `llama3.1:8b` + `qwen2.5:7b`), LM Studio installed. Write a script that calls both via LangChain's OpenAI-compatible endpoint. Prompt-engineering speedrun: Anthropic's interactive tutorial, do the exercises you can't already do. |
| **Wed** | 2h | **Ed Donner Core — selective.** Watch the frontier-vs-open-source + Hugging Face pipeline sections at 1.75×. Build his Day-1-style summarizer *against Ollama*, then extend it to summarize a real doc from your capstone corpus. |
| **Thu** | 2h | **Structured outputs + tool calling.** LangChain docs: structured output (Pydantic) + `bind_tools`. Build a script where the model calls one Python function (e.g., fetch a WordPress plugin changelog). This is the atom of everything in Weeks 3–4. |
| **Fri** | 2h | **Gradio + capstone skeleton.** Simple Gradio chat UI over your local model. Create the capstone repo structure: `ingestion/`, `rag/`, `agent/`, `mcp_server/`, `eval/`. Collect the raw corpus (docs/PDFs/pages for Option A or synthetic records for Option B). |
| **Sat** | 2.5h | **QLoRA — touch, don't marry.** Run Ed Donner's fine-tuning notebook once (Colab free tier or local if your GPU allows). Goal: you can explain what QLoRA does, when fine-tuning beats RAG, and you've run it once. **Timebox: 2.5h, no rabbit holes.** |
| **Sun** | 2.5h | **Naive RAG v0.** LangChain RAG tutorial applied to your capstone corpus: load → recursive chunking → local embeddings (`nomic-embed-text` via Ollama) → Chroma → retrieval chain in the Gradio UI. It will be mediocre. That's the point — Week 2 fixes it measurably. |

**✅ Week 1 DoD:** Capstone repo has a working (naive) RAG chatbot on a local model, you've run QLoRA once, and you can explain the Phase-0 concepts aloud.

---

## 📅 WEEK 2 — RAG Mastery (15h)

**Goal:** turn RAG v0 into RAG you can *defend* — and prove the improvement with numbers. This is the highest-ROI FDE week: RAG quality is where customer projects live or die.

| Session | Hours | Do this |
|---|---|---|
| **Mon** | 2h | **Chunking strategies.** Implement a second strategy (semantic or parent-document) alongside recursive. Read Anthropic's Contextual Retrieval post (15 min) and note where it would apply. |
| **Tue** | 2h | **Eval harness FIRST.** Write 15–20 labeled Q&A pairs from your corpus. Set up RAGAS (faithfulness, answer relevancy, context precision/recall) against a local or cheap model as judge. Score RAG v0 — record the baseline. |
| **Wed** | 2h | **Hybrid retrieval.** Add BM25 alongside dense retrieval (LangChain `EnsembleRetriever`). Understand *when* sparse wins (exact terms, error codes, API names — very relevant to Option A). Re-run RAGAS. |
| **Thu** | 2h | **Reranking.** Add a cross-encoder reranker (local `bge-reranker` via sentence-transformers — free). Re-run RAGAS. This is usually the single biggest accuracy jump; screenshot the before/after. |
| **Fri** | 2h | **Query transformation.** Add multi-query or HyDE for vague questions. Compare chunking strategy A vs B with final pipeline. Lock in the winner. |
| **Sat** | 2.5h | **DeepLearning.AI — "Building and Evaluating Advanced RAG"** (short course, ~2h at speed). You've now built most of it, so this consolidates and fills gaps rather than teaches from zero. |
| **Sun** | 2.5h | **Write it up.** `rag/README.md`: architecture, the RAGAS score table (v0 → hybrid → reranked → final), and one paragraph on the build-vs-buy question (hand-rolled vs Bedrock Knowledge Bases — you'll test the managed side in Week 4). Buffer time for anything that slipped. |

**✅ Week 2 DoD:** You can take a RAG pipeline giving wrong answers and diagnose chunking vs retrieval vs reranking vs generation — and you have a RAGAS table proving you improved yours.

---

## 📅 WEEK 3 — LangGraph Agents + Your MCP Server (15h)

**Goal:** the two skills FDE interviews probe hardest — agent orchestration and integration. Split the week: agents Mon–Wed, MCP Thu–Sun.

| Session | Hours | Do this |
|---|---|---|
| **Mon** | 2h | **Agent patterns + LangGraph basics.** Read Anthropic's "Building Effective Agents" essay (do not skip — read it properly, it's the best 45 min in this plan). Then LangGraph quickstart: nodes, edges, state. Be able to explain Reflection / Tool Use / Planning / Multi-Agent with one real example each. |
| **Tue** | 2h | **LangChain Academy "Intro to LangGraph"** — modules 1–2 only, at speed, coding along against Ollama. Skip what you already did Monday. |
| **Wed** | 2h | **Capstone agent layer.** Build the multi-agent graph: router node → RAG-answer node (your Week-2 pipeline as a tool) → one specialist node (troubleshooter / consent-checker) → responder. Add a **checkpointer** for conversation memory. |
| **Thu** | 2h | **MCP concepts + first server.** Anthropic's "Introduction to MCP" course (skim to the Python server-building units). Scaffold your server with **FastMCP**: define 3 tools + 1 resource against your real API (Option A: Meta Graph API test number; Option B: synthetic records store). |
| **Fri** | 2h | **Finish + debug the server.** All tools working. Debug with **MCP Inspector** (`npx @modelcontextprotocol/inspector`). Understand stdio vs Streamable HTTP — implement stdio now, note the HTTP path for deploy. |
| **Sat** | 2.5h | **Connect to two hosts.** (1) Claude Desktop — config, watch Claude call your tools. (2) Your LangGraph agent — via the MCP adapter so agent nodes can invoke server tools. This "one server, two hosts" demo is the whole point of MCP; screen-record 60 seconds of it now for the demo video. |
| **Sun** | 2.5h | **Integration pass.** Full capstone flow end-to-end locally: user question → router → RAG answer with citations → action via MCP tool → response. Fix the seams. Commit + short write-up. |

**✅ Week 3 DoD:** Working multi-agent LangGraph app with memory, calling a custom MCP server you built, which also works in Claude Desktop — and you can explain Tools vs Resources vs Prompts and stdio vs HTTP without notes.

---

## 📅 WEEK 4 — Bedrock Deploy + Production Layer + Polish (15h)

**Goal:** ship it to your professional cloud, wrap it in production hygiene, and package it to sell you. Use the **office AWS account**; set a billing alarm the day you start; tear down after sessions.

| Session | Hours | Do this |
|---|---|---|
| **Mon** | 2h | **Bedrock foundations.** Model access requested (do this FIRST — approval can lag). Invoke Claude Haiku / Nova-lite via `boto3` and via LangChain's `ChatBedrockConverse`. Swap your capstone's local model for Bedrock with a one-line change — the payoff of the OpenAI-compatible discipline. Budget slack for IAM friction; wrestling IAM *is* FDE training. |
| **Tue** | 2h | **Bedrock Knowledge Base.** Stand one up over your corpus (S3 → KB). Query it; run your RAGAS set against it vs your hand-built pipeline. Now you can argue build-vs-buy with *your own data* — a core FDE conversation. |
| **Wed** | 2h | **AgentCore Runtime deploy.** AgentCore CLI quickstart, then deploy your LangGraph agent to Runtime (AgentCore supports LangGraph directly). Get one end-to-end cloud invocation working. |
| **Thu** | 2h | **Gateway + Memory.** Expose your MCP server's tools via **AgentCore Gateway**; add **AgentCore Memory** for session state. If Gateway fights you, fallback: run the MCP server alongside and document the Gateway path — don't burn the week here. |
| **Fri** | 2h | **Guardrails + tracing.** Bedrock Guardrails (PII + topic filters) on the deployed agent. Wire **Langfuse** (self-host via Docker) or LangSmith into the local version; inspect one full trace of a multi-node run. |
| **Sat** | 2.5h | **ADK taster (kept, as you asked — but capped).** ADK quickstart: one single agent with one custom tool, run in `adk web`, inspect the execution. Goal is conversant-not-expert: you can compare ADK's `Agent`/`Workflow` model to LangGraph in an interview. **Hard cap 2.5h**; full ADK + Vertex deploy is Month 2. |
| **Sun** | 2.5h | **Package it.** Capstone README (problem → architecture → tradeoffs → results table), Mermaid architecture diagram, 3-min Loom demo (local flow + Claude Desktop MCP + cloud invocation), pin the repo. Then do one 30-min FDE rep: take a vague prompt ("our clinic's front desk is drowning in WhatsApp messages") and sketch an architecture + riskiest assumption on paper. |

**✅ Week 4 DoD:** Capstone deployed on AgentCore with a Knowledge Base comparison, guardrails, and a trace you can walk through; repo polished with diagram + demo video; ADK at conversational depth.

---

## ✅ End-of-Month FDE Scorecard (the compressed checklist)

- [ ] Build RAG from scratch and improve RAGAS scores measurably ← Week 2
- [ ] Justify chunking/embedding/retrieval/reranking choices ← Week 2
- [ ] Explain + implement the 4 agent patterns ← Week 3
- [ ] Multi-agent system in LangGraph with memory + custom tools ← Week 3
- [ ] Build, debug, connect a custom MCP server to 2 hosts ← Week 3
- [ ] Run QLoRA once and explain fine-tune vs RAG ← Week 1
- [ ] Deploy an agent on AWS (AgentCore Runtime) ← Week 4
- [ ] Managed RAG (Knowledge Base) + build-vs-buy argument with your own numbers ← Week 4
- [ ] Guardrails + tracing on a real system ← Week 4
- [ ] Explain RAG/agents/MCP to a non-technical stakeholder ← README + Loom
- [ ] Scope a fuzzy problem into an architecture in 30 min ← Week 4 Sunday rep (keep doing weekly)

---

## 📦 Month-2 Backlog (what we deferred — deliberately)

Do these *after* the month, in roughly this order:

1. **Ed Donner Agentic + Production tracks in full** — you now have the context to move through them fast.
2. **Google ADK deep dive + Vertex Agent Engine / Cloud Run deploy** — turns "conversant" into the multi-cloud story ("same system on both clouds").
3. **Karpathy — build GPT from scratch** — deepest foundation payoff, weekend project.
4. **Anthropic MCP Advanced Topics** + Streamable HTTP deploy of your server (behind AgentCore Gateway properly).
5. **CI-gated evals + runbook** (GitHub Actions running RAGAS/DeepEval on PRs).
6. **GraphRAG / contextual retrieval implementation**, HF Agents course for framework breadth (smolagents/LlamaIndex), Strands Agents comparison.
7. **Weekly FDE reps forever:** one 30-min "scope a vague problem" exercise + one short write-up/LinkedIn post per shipped feature.

---

## 🔗 Links Actually Used This Month

- 3B1B GPT/Attention: <https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi>
- Illustrated Transformer: <https://jalammar.github.io/illustrated-transformer/>
- Anthropic prompt engineering: <https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview>
- Ed Donner Core (selective): <https://www.udemy.com/course/llm-engineering-master-ai-and-large-language-models/> · code: <https://github.com/ed-donner/llm_engineering>
- LangChain RAG tutorial: <https://python.langchain.com/docs/tutorials/rag/>
- RAGAS: <https://docs.ragas.io/>
- Contextual Retrieval: <https://www.anthropic.com/news/contextual-retrieval>
- DL.AI Building & Evaluating Advanced RAG: <https://www.deeplearning.ai/short-courses/>
- Building Effective Agents (read twice): <https://www.anthropic.com/engineering/building-effective-agents>
- LangGraph docs: <https://langchain-ai.github.io/langgraph/> · Academy: <https://academy.langchain.com/>
- MCP: <https://modelcontextprotocol.io/> · Anthropic intro course: <https://anthropic.skilljar.com/introduction-to-model-context-protocol> · Python SDK/FastMCP: <https://github.com/modelcontextprotocol/python-sdk>
- Bedrock user guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/>
- AgentCore guide: <https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html> · CLI quickstart: <https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-get-started-cli.html>
- Langfuse: <https://langfuse.com/docs>
- ADK quickstart: <https://google.github.io/adk-docs/>

---

## 🧭 If You Slip (you will, once)

- **Behind by ≤2h:** steal from the weekend session, cut video time first, never cut build time.
- **Behind by a full week:** drop the ADK taster and the QLoRA session (they're the only non-load-bearing blocks) and compress Week 2 Sat into 1h.
- **Non-negotiables that survive any slip:** RAGAS-evaluated RAG, the LangGraph agent, the MCP server on two hosts, and one AgentCore deploy. Those four ARE the FDE story.

*Ship the capstone. Everything else is negotiable.*
