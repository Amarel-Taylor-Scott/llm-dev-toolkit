#!/usr/bin/env python3
"""Generate the LLM Dev Toolkit index from the autopilot ledger.

This suite is a living catalog: it reads which tools the autonomous loop has
published and rebuilds README.md so the toolkit stays current as new tools ship.
Re-run it any time (the autopilot also calls it after publishing a new tool).
"""

from __future__ import annotations

import json
import os
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
LEDGER = os.path.join(ROOT, "dev_loop", "autopilot", "ledger.jsonl")
OWNER = "Amarel-Taylor-Scott"

# Keywords that mark a tool as part of the LLM/agent builder kit (vs general util).
LLM_KW = ("llm", "prompt", "rag", "agent", "token", "model", "eval", "embedding",
          "context", "chat", "inference", "capability", "schema", "trace", "cost")

# Hand-built flagships (not from the autopilot ledger) — larger systems.
FLAGSHIPS = [
    {"slug": "hybrid-graph-mapper",
     "repo_url": f"https://github.com/{OWNER}/hybrid-graph-mapper",
     "description": "Build a knowledge graph of code or documents by fusing deterministic parsing, NLP, and LLM discovery — provenance-aware, both-context edge scoring"},
    {"slug": "contradiction-mapper",
     "repo_url": f"https://github.com/{OWNER}/contradiction-mapper",
     "description": "LLM codegraph harness that reviews every function/file for contradictions (intent vs implementation, cross-codebase conflicts) with chunking + second-model verify"},
    {"slug": "pyprefix",
     "repo_url": f"https://github.com/{OWNER}/pyprefix",
     "description": "Typed, greppable Python names (py_class_/py_function_/py_method_/py_inst_) for deterministic search + code maps — checker + verified codemod + map"},
    {"slug": "cot-contracts",
     "repo_url": f"https://github.com/{OWNER}/cot-contracts",
     "description": "Design-by-contract for reasoning: declare + ENFORCE the chain of thought a model must follow (steps/order/gates/tools), verify clause-by-clause with a cross-model judge, export conformant traces as LoRA data"},
    {"slug": "docdense",
     "repo_url": f"https://github.com/{OWNER}/docdense",
     "description": "Intake doc websites → dense, chunked, LLM-ready text deterministically (stdlib): strip HTML boilerplate, densify, heading-aware chunk — 61-75% fewer tokens, no LLM spent on raw HTML"},
    {"slug": "repoprompt",
     "repo_url": f"https://github.com/{OWNER}/repoprompt",
     "description": "Pack a code repo into one LLM-ready prompt — gitignore-aware, token-budgeted, file tree + fenced files, Python signatures-only map mode (the code sibling of docdense)"},
    {"slug": "llmjson",
     "repo_url": f"https://github.com/{OWNER}/llmjson",
     "description": "Extract & repair JSON from messy LLM output — fenced blocks, trailing commas, single quotes, True/None, comments, truncated/streamed — deterministically, stdlib only"},
    {"slug": "streamjson",
     "repo_url": f"https://github.com/{OWNER}/streamjson",
     "description": "Incrementally parse partial / streaming JSON (LLM token streams, SSE) — best-effort object from incomplete JSON, and emit array items / OpenAI deltas as they complete"},
    {"slug": "diffapply",
     "repo_url": f"https://github.com/{OWNER}/diffapply",
     "description": "Robustly apply edits LLMs emit — unified diffs AND search/replace blocks — with fuzzy context matching and a never-corrupt-on-failure guarantee"},
    {"slug": "ftprep",
     "repo_url": f"https://github.com/{OWNER}/ftprep",
     "description": "Fine-tune / LoRA dataset prep for JSONL — convert between chat/instruction/completion, dedup, deterministic train/val/test split, validate, stats"},
    {"slug": "toolschema",
     "repo_url": f"https://github.com/{OWNER}/toolschema",
     "description": "Turn a Python function into an OpenAI/Anthropic tool (function-calling) JSON schema from its signature + docstring, and dispatch validated tool calls back to it"},
    {"slug": "secretscan",
     "repo_url": f"https://github.com/{OWNER}/secretscan",
     "description": "Detect & redact secrets + PII in text/files/diffs before they reach an LLM or a commit — entropy + Luhn gated to cut false positives"},
    {"slug": "injectguard",
     "repo_url": f"https://github.com/{OWNER}/injectguard",
     "description": "Heuristic prompt-injection / jailbreak detector for untrusted content (retrieved docs, tool output) — categorized patterns, risk score, invisible-char stripping"},
    {"slug": "promptcache",
     "repo_url": f"https://github.com/{OWNER}/promptcache",
     "description": "File-backed cache for LLM responses — exact + near-duplicate (MinHash) prompt matching to skip paying for repeat calls"},
    {"slug": "neardupe",
     "repo_url": f"https://github.com/{OWNER}/neardupe",
     "description": "Find near-duplicate texts in a dataset (beyond exact dedup) via MinHash + LSH banding — dataset hygiene for training / RAG corpora"},
    {"slug": "bm25lite",
     "repo_url": f"https://github.com/{OWNER}/bm25lite",
     "description": "Reusable, persistable Okapi BM25 lexical search index for RAG/retrieval — build, query, save/load, no dependencies"},
    {"slug": "chunklib",
     "repo_url": f"https://github.com/{OWNER}/chunklib",
     "description": "General token-aware chunker for text + code (AST-aware, never splits a function) + markdown — the reusable chunking primitive for RAG"},
    {"slug": "mdextract",
     "repo_url": f"https://github.com/{OWNER}/mdextract",
     "description": "Pull structured pieces out of LLM Markdown — code blocks by language, GFM tables as dicts, heading outline, lists, links, front-matter — no markdown lib"},
    {"slug": "tagextract",
     "repo_url": f"https://github.com/{OWNER}/tagextract",
     "description": "Tolerantly extract content from XML-ish tags LLMs emit (<answer>, <thinking>) — nested, unclosed, attributes — without an XML parser"},
    {"slug": "textmetrics",
     "repo_url": f"https://github.com/{OWNER}/textmetrics",
     "description": "Text-comparison metrics for evaluating LLM output — exact match, token-F1, BLEU, ROUGE-N/L, edit distance, WER/CER — no dependencies"},
]


def load_published() -> list:
    out = []
    if os.path.exists(LEDGER):
        for ln in open(LEDGER, encoding="utf-8"):
            ln = ln.strip()
            if not ln:
                continue
            r = json.loads(ln)
            if r.get("status") == "published" and r.get("repo_url"):
                out.append(r)
    return out


def is_llm_tool(r: dict) -> bool:
    if r.get("origin") == "research-radar":
        return True
    blob = (r.get("slug", "") + " " + r.get("title", "") + " " +
            r.get("description", "")).lower()
    return any(k in blob for k in LLM_KW)


def _row(r: dict) -> str:
    desc = (r.get("description", "") or r.get("title", "")).split(".")[0][:96]
    imp = f" · _improved ×{r['improvements']}_" if r.get("improvements") else ""
    return f"| [`{r['slug']}`]({r['repo_url']}) | {desc}{imp} |"


def render(pub: list) -> str:
    llm = sorted([r for r in pub if is_llm_tool(r)], key=lambda r: r["slug"])
    util = sorted([r for r in pub if not is_llm_tool(r)], key=lambda r: r["slug"])
    n = len(pub)
    out = []
    out.append("# LLM Dev Toolkit")
    out.append("")
    out.append("> A growing, MIT-licensed collection of small, **dependency-free "
               "Python** tools for building LLM & agent applications — the picks "
               "and shovels. Each is its own repo; this is the index.")
    out.append("")
    out.append(f"**{len(llm)} LLM/agent tools** · **{len(util)} general "
               f"utilities** · stdlib-only · MIT")
    out.append("")
    out.append("These tools are produced by an **autonomous research → implement "
               "→ publish loop**: a radar scrapes the AI space for what's "
               "trending, a fleet of code models build and *verify* the tools, "
               "and a second model audits each one for gamed tests before it "
               "ships. This index rebuilds itself as new tools land.")
    out.append("")
    out.append("## 🚩 Flagships")
    out.append("")
    out.append("| Project | What it does |")
    out.append("|---|---|")
    out += [_row(r) for r in FLAGSHIPS]
    out.append("")
    out.append("## 🧰 LLM & agent tools")
    out.append("")
    out.append("| Tool | What it does |")
    out.append("|---|---|")
    out += [_row(r) for r in llm]
    if util:
        out.append("")
        out.append("## 🔧 General utilities")
        out.append("")
        out.append("| Tool | What it does |")
        out.append("|---|---|")
        out += [_row(r) for r in util]
    out.append("")
    out.append("## Install")
    out.append("")
    out.append("Each tool is stdlib-only — clone and run, no dependencies:")
    out.append("")
    out.append("```bash")
    out.append(f"git clone https://github.com/{OWNER}/<tool>.git")
    out.append("```")
    out.append("")
    out.append("(PyPI releases are prepared — `pip install <tool>` once tokens "
               "are wired.)")
    out.append("")
    out.append("## How this was built")
    out.append("")
    out.append("Fully autonomously, with quality gates after DeepReinforce's "
               "Ornith-1.0 reward-hacking defense: deterministic re-verification "
               "of every build, a monitor that rejects tautological tests, and a "
               "cross-model judge veto. Nothing broken or self-gamed ships.")
    out.append("")
    out.append(dim_footer(n))
    return "\n".join(out)


def dim_footer(n: int) -> str:
    return (f"<sub>Auto-generated from {n} published repositories · "
            f"{time.strftime('%Y-%m-%d')}</sub>")


def main() -> int:
    pub = load_published()
    readme = render(pub)
    with open(os.path.join(HERE, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme + "\n")
    print(f"wrote README.md — {len(pub)} tools "
          f"({sum(1 for r in pub if is_llm_tool(r))} LLM/agent)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
