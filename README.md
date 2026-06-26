# LLM Dev Toolkit

> A growing, MIT-licensed collection of small, **dependency-free Python** tools for building LLM & agent applications — the picks and shovels. Each is its own repo; this is the index.

**10 LLM/agent tools** · **3 general utilities** · stdlib-only · MIT

These tools are produced by an **autonomous research → implement → publish loop**: a radar scrapes the AI space for what's trending, a fleet of code models build and *verify* the tools, and a second model audits each one for gamed tests before it ships. This index rebuilds itself as new tools land.

## 🧰 LLM & agent tools

| Tool | What it does |
|---|---|
| [`agent-trace-scorer`](https://github.com/Amarel-Taylor-Scott/agent-trace-scorer) | Reads JSONL agent traces where each line has {step, tool, input, output, status, answer} |
| [`capability-manifest-validator`](https://github.com/Amarel-Taylor-Scott/capability-manifest-validator) | Validates a JSON agent skill manifest: required fields (name, version, skills with triggers), no |
| [`llm-cost-calc`](https://github.com/Amarel-Taylor-Scott/llm-cost-calc) | Compute and compare LLM API costs from token counts across a built-in price table (per-model inp · _improved ×1_ |
| [`model-footprint-estimator`](https://github.com/Amarel-Taylor-Scott/model-footprint-estimator) | Estimates GGUF file size and inference RAM from parameters, quantization bits, context length, a |
| [`multi-agent-debate-simulator`](https://github.com/Amarel-Taylor-Scott/multi-agent-debate-simulator) | Simulates N agents with deterministic role policies passing messages in rounds until consensus o |
| [`prompt-lint`](https://github.com/Amarel-Taylor-Scott/prompt-lint) | Lint prompt templates: detect unfilled {slots}, unbalanced braces, injection-risky phrases, and  · _improved ×1_ |
| [`prompt-template-linter`](https://github.com/Amarel-Taylor-Scott/prompt-template-linter) | Parses a system prompt template string, finds {{placeholder}} patterns, counts instructions (lin |
| [`rag-chunk-ranker`](https://github.com/Amarel-Taylor-Scott/rag-chunk-ranker) | Given a query string and a list of text chunks, compute BM25-like relevance scores using only co |
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

<sub>Auto-generated from 13 published repositories · 2026-06-26</sub>
