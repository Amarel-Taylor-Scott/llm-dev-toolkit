# LLM Dev Toolkit

> A growing, MIT-licensed collection of small, **dependency-free Python** tools for building LLM & agent applications — the picks and shovels. Each is its own repo; this is the index.

**13 LLM/agent tools** · **7 agent-systems primitives + 3 numpy ML (new: Waves 7-9)** · **3 general utilities** · stdlib-only (+ numpy ML) · MIT

These tools are produced by an **autonomous research → implement → publish loop**: a radar scrapes the AI space for what's trending, a fleet of code models build and *verify* the tools, and a second model audits each one for gamed tests before it ships. This index rebuilds itself as new tools land.

## 🚩 Flagships

| Project | What it does |
|---|---|
| [`hybrid-graph-mapper`](https://github.com/Amarel-Taylor-Scott/hybrid-graph-mapper) | Build a knowledge graph of code or documents by fusing deterministic parsing, NLP, and LLM disco |
| [`contradiction-mapper`](https://github.com/Amarel-Taylor-Scott/contradiction-mapper) | LLM codegraph harness that reviews every function/file for contradictions (intent vs implementat |
| [`pyprefix`](https://github.com/Amarel-Taylor-Scott/pyprefix) | Typed, greppable Python names (py_class_/py_function_/py_method_/py_inst_) for deterministic sea |
| [`cot-contracts`](https://github.com/Amarel-Taylor-Scott/cot-contracts) | Design-by-contract for reasoning: declare + ENFORCE the chain of thought a model must follow (st |
| [`docdense`](https://github.com/Amarel-Taylor-Scott/docdense) | Intake doc websites → dense, chunked, LLM-ready text deterministically (stdlib): strip HTML boil |
| [`repoprompt`](https://github.com/Amarel-Taylor-Scott/repoprompt) | Pack a code repo into one LLM-ready prompt — gitignore-aware, token-budgeted, file tree + fenced |
| [`llmjson`](https://github.com/Amarel-Taylor-Scott/llmjson) | Extract & repair JSON from messy LLM output — fenced blocks, trailing commas, single quotes, Tru |
| [`streamjson`](https://github.com/Amarel-Taylor-Scott/streamjson) | Incrementally parse partial / streaming JSON (LLM token streams, SSE) — best-effort object from  |
| [`diffapply`](https://github.com/Amarel-Taylor-Scott/diffapply) | Robustly apply edits LLMs emit — unified diffs AND search/replace blocks — with fuzzy context ma |
| [`ftprep`](https://github.com/Amarel-Taylor-Scott/ftprep) | Fine-tune / LoRA dataset prep for JSONL — convert between chat/instruction/completion, dedup, de |
| [`toolschema`](https://github.com/Amarel-Taylor-Scott/toolschema) | Turn a Python function into an OpenAI/Anthropic tool (function-calling) JSON schema from its sig |
| [`secretscan`](https://github.com/Amarel-Taylor-Scott/secretscan) | Detect & redact secrets + PII in text/files/diffs before they reach an LLM or a commit — entropy |
| [`injectguard`](https://github.com/Amarel-Taylor-Scott/injectguard) | Heuristic prompt-injection / jailbreak detector for untrusted content (retrieved docs, tool outp |
| [`promptcache`](https://github.com/Amarel-Taylor-Scott/promptcache) | File-backed cache for LLM responses — exact + near-duplicate (MinHash) prompt matching to skip p |
| [`neardupe`](https://github.com/Amarel-Taylor-Scott/neardupe) | Find near-duplicate texts in a dataset (beyond exact dedup) via MinHash + LSH banding — dataset  |
| [`bm25lite`](https://github.com/Amarel-Taylor-Scott/bm25lite) | Reusable, persistable Okapi BM25 lexical search index for RAG/retrieval — build, query, save/loa |
| [`chunklib`](https://github.com/Amarel-Taylor-Scott/chunklib) | General token-aware chunker for text + code (AST-aware, never splits a function) + markdown — th |
| [`mdextract`](https://github.com/Amarel-Taylor-Scott/mdextract) | Pull structured pieces out of LLM Markdown — code blocks by language, GFM tables as dicts, headi |
| [`tagextract`](https://github.com/Amarel-Taylor-Scott/tagextract) | Tolerantly extract content from XML-ish tags LLMs emit (<answer>, <thinking>) — nested, unclosed |
| [`textmetrics`](https://github.com/Amarel-Taylor-Scott/textmetrics) | Text-comparison metrics for evaluating LLM output — exact match, token-F1, BLEU, ROUGE-N/L, edit |
| [`prompttmpl`](https://github.com/Amarel-Taylor-Scott/prompttmpl) | Tiny dependency-free prompt template engine — placeholders+defaults, conditionals, loops, partia |
| [`chatwindow`](https://github.com/Amarel-Taylor-Scott/chatwindow) | Token-aware trimming of chat history to fit a context window — keep system + recent turns, drop  |
| [`chatconv`](https://github.com/Amarel-Taylor-Scott/chatconv) | Convert chat transcripts between OpenAI, Anthropic, ShareGPT, and Markdown formats |
| [`ctxfit`](https://github.com/Amarel-Taylor-Scott/ctxfit) | Select which scored context items to put in a limited context window — greedy value-density or o |
| [`fewshot`](https://github.com/Amarel-Taylor-Scott/fewshot) | Dynamically select the best few-shot examples for a prompt — similarity ranking + MMR diversity, |

## 🤖 ML toolkit (numpy)

Larger ML systems for honest modeling under distribution shift — the one place a dependency (numpy) is warranted.

| Project | What it does |
|---|---|
| [`shiftblend`](https://github.com/Amarel-Taylor-Scott/shiftblend) | Honest model exploration under covariate shift — score recipes by transferable skill (not in-sam |
| [`waveweight`](https://github.com/Amarel-Taylor-Scott/waveweight) | Discover sample-weight schemes (index patterns + data-driven local-window drivers × curves) that |
| [`stablefit`](https://github.com/Amarel-Taylor-Scott/stablefit) | Jointly learn sample + feature weights to minimize the train-CV gap (stability / anti-overfit) — |
| [`densityweight`](https://github.com/Amarel-Taylor-Scott/densityweight) | Downweight redundant dense regions so clustered near-duplicate rows do not dominate a fit — effe |
| [`neighborweight`](https://github.com/Amarel-Taylor-Scott/neighborweight) | Weight samples from feature-space neighbor behavior — isolate outliers, local target disagreemen |
| [`bootweight`](https://github.com/Amarel-Taylor-Scott/bootweight) | Per-sample weights from bootstrap out-of-bag stability — downweight rows with persistently large |
| [`chunkweight`](https://github.com/Amarel-Taylor-Scott/chunkweight) | Weight samples by chunk behavior — contiguous/interleaved/cluster chunks scored by leave-chunk-o |
| [`influenceweight`](https://github.com/Amarel-Taylor-Scott/influenceweight) | Closed-form ridge influence weighting — leverage, exact leave-one-out residual, and Cook's dista |
| [`weightmap`](https://github.com/Amarel-Taylor-Scott/weightmap) | Learn a shallow interpretable map from row-driver features to sample weights, catching driver in |
| [`shiftweight`](https://github.com/Amarel-Taylor-Scott/shiftweight) | Covariate-shift correction by adversarial validation — features-only propensities weight train r |
| [`groupweight`](https://github.com/Amarel-Taylor-Scott/groupweight) | Weight whole feature groups by cross-fold contribution to generalization — group-level shrinkage |
| [`driftweight`](https://github.com/Amarel-Taylor-Scott/driftweight) | Recency sample weighting for regime drift — select how strongly to favor recent rows on train on |
| [`weightfuse`](https://github.com/Amarel-Taylor-Scott/weightfuse) | Fuse sample-weight signals such as recency and residual stability, then require the fused vector |
| [`gapservo`](https://github.com/Amarel-Taylor-Scott/gapservo) | Gap-aware gradient descent — a live cross-validated generalization-gap instrument + a guarded CV-gap stopper that cuts overfitting in one online pass (~2× under real overfitting, neutral otherwise); held-out + null + true-negative controls _(new)_ |
| [`deltamem`](https://github.com/Amarel-Taylor-Scott/deltamem) | Gated delta-rule fast-weight associative memory — the mechanism behind linear attention & BDH-style synaptic memory, with additive-Hebbian / delta / gated-delta rules and honest measurements of when each helps (single-pass Hebbian is competitive; delta wins on refinement + overwrite) _(new)_ |
| [`indextune`](https://github.com/Amarel-Taylor-Scott/indextune) | Self-tune a semantic retrieval index — search (embedder × dimensionality × LSH bits/tables × metric) for the config that retrieves best on held-out queries within a candidate-cost budget; the self-tuning layer for semantic-linker, with a random-config control (tuned ~2× an untuned default, 10× fewer candidates) _(new)_ |

## 🧩 Agent systems & primitives

Sans-IO building blocks for agent/LLM systems — deterministic, dependency-free, and heavily property-tested. _(new this wave — pending push)_

| Project | What it does |
|---|---|
| [`effectgen`](https://github.com/Amarel-Taylor-Scott/effectgen) | Algebraic effects via generators — write agent logic as pure generators that `yield` effect requests; handlers decide meaning (real IO, mocks, record, replay). Test agents with no APIs; reproduce bugs exactly. 72 tests |
| [`agenttape`](https://github.com/Amarel-Taylor-Scott/agenttape) | A VCR + delta-debugger for tool-call loops — record calls to a tape, replay offline, localize the first divergence, and ddmin-minimize a 400-call failure to the 3 calls that reproduce it. 63 tests |
| [`toolgate`](https://github.com/Amarel-Taylor-Scott/toolgate) | A capability firewall for tool calls — declarative allow/deny/confirm/dry-run/redact policy + budgets, and mutating calls wrapped in transactions with a policy-checked undo journal (plan-then-commit). 74 tests |
| [`stepcache`](https://github.com/Amarel-Taylor-Scott/stepcache) | Content-addressed incremental recomputation — a Salsa-style runtime that hashes each pipeline step and reruns only the dirty cone, proving what was cached vs computed and why. 65 tests |
| [`crdtext`](https://github.com/Amarel-Taylor-Scott/crdtext) | A convergent replicated text type (RGA CRDT) — N replicas edit concurrently, exchange ops in any order (delayed/duplicated), and provably converge. 100-scenario convergence proof. 32 tests |
| [`backcheck`](https://github.com/Amarel-Taylor-Scott/backcheck) | Trust-but-verify overrides via held-out backtesting — before a candidate predictor overrides your default, backtest it on a held-out slice of that instance's ground truth and accept only on a consistent margin; tail-holdout predicts deployment/extrapolation error 8× better than random (0.50 vs 0.06). 23 tests |
| [`metamorph`](https://github.com/Amarel-Taylor-Scott/metamorph) | Metamorphic testing without an oracle — verify functions you can't write expected outputs for by stating how the output must CHANGE under an input transform (permutation-invariance, shift-equivariance); catches bugs example tests miss and shrinks counterexamples to minimal inputs. 21 tests |

## 🧰 LLM & agent tools

| Tool | What it does |
|---|---|
| [`agent-trace-scorer`](https://github.com/Amarel-Taylor-Scott/agent-trace-scorer) | Reads JSONL agent traces where each line has {step, tool, input, output, status, answer} · _improved ×1_ |
| [`agent-trace-validator`](https://github.com/Amarel-Taylor-Scott/agent-trace-validator) | Parse a JSON agent trace (steps with tool calls, inputs, outputs, and durations), validate that  |
| [`capability-manifest-validator`](https://github.com/Amarel-Taylor-Scott/capability-manifest-validator) | Validates a JSON agent skill manifest: required fields (name, version, skills with triggers), no |
| [`llm-cost-calc`](https://github.com/Amarel-Taylor-Scott/llm-cost-calc) | Compute and compare LLM API costs from token counts across a built-in price table (per-model inp · _improved ×1_ |
| [`model-footprint-estimator`](https://github.com/Amarel-Taylor-Scott/model-footprint-estimator) | Estimates GGUF file size and inference RAM from parameters, quantization bits, context length, a |
| [`multi-agent-debate-simulator`](https://github.com/Amarel-Taylor-Scott/multi-agent-debate-simulator) | Simulates N agents with deterministic role policies passing messages in rounds until consensus o · _improved ×1_ |
| [`prompt-diff-linter`](https://github.com/Amarel-Taylor-Scott/prompt-diff-linter) | A small tool that compares two prompt template files, lists added/removed placeholders, detects  |
| [`prompt-lint`](https://github.com/Amarel-Taylor-Scott/prompt-lint) | Lint prompt templates: detect unfilled {slots}, unbalanced braces, injection-risky phrases, and  · _improved ×1_ |
| [`prompt-template-linter`](https://github.com/Amarel-Taylor-Scott/prompt-template-linter) | Parses a system prompt template string, finds {{placeholder}} patterns, counts instructions (lin · _improved ×1_ |
| [`rag-chunk-ranker`](https://github.com/Amarel-Taylor-Scott/rag-chunk-ranker) | Given a query string and a list of text chunks, compute BM25-like relevance scores using only co · _improved ×1_ |
| [`rag-chunk-scorer`](https://github.com/Amarel-Taylor-Scott/rag-chunk-scorer) | Simulate a RAG retriever without a model: chunk documents using fixed-size, paragraph, and sente |
| [`token-budget-guard`](https://github.com/Amarel-Taylor-Scott/token-budget-guard) | A stdlib-only CLI that reads a prompt file and a model config JSON (max_tokens, price_per_1k, co · _improved ×1_ |
| [`token-cost-estimator`](https://github.com/Amarel-Taylor-Scott/token-cost-estimator) | A stdlib-only CLI that reads a JSONL of request/response strings, estimates token counts using a |

## 🔧 General utilities

| Tool | What it does |
|---|---|
| [`humanbytes-cli`](https://github.com/Amarel-Taylor-Scott/humanbytes-cli) | A tiny library + CLI to parse and format human-readable byte sizes ('1 · _improved ×1_ |
| [`jsonl-stats`](https://github.com/Amarel-Taylor-Scott/jsonl-stats) | A CLI that reports stats over a JSONL file: record count, key frequency, and per-key type histog · _improved ×1_ |
| [`retry-backoff`](https://github.com/Amarel-Taylor-Scott/retry-backoff) | A dependency-free retry decorator with exponential backoff, jitter, and an exception allowlist · _improved ×1_ |

## Install

Each tool is stdlib-only — clone and run, no dependencies:

```bash
git clone https://github.com/Amarel-Taylor-Scott/<tool>.git
```

(PyPI releases are prepared — `pip install <tool>` once tokens are wired.)

## How this was built

Fully autonomously, with quality gates after DeepReinforce's Ornith-1.0 reward-hacking defense: deterministic re-verification of every build, a monitor that rejects tautological tests, and a cross-model judge veto. Nothing broken or self-gamed ships.

<sub>Auto-generated from 16 published repositories · 2026-07-09</sub>
