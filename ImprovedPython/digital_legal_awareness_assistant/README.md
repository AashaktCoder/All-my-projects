# Digital Legal Awareness Assistant & KYR Framework

A working Python prototype for the Smart India Hackathon project:

> Digital Legal Awareness Assistant & KYR Framework for Small Institutions

---

## Architecture

Institution Rulebook

        ↓

PDF Extraction / OCR

        ↓

Rule Processing

        ↓

Knowledge Base

        ↓

Sentence Transformer Embeddings

        ↓

FAISS Vector Search

        ↓

Relevant Rules

        ↓

LLM

        ↓

AI Response

        ↓

KYR Guidance + Sources


If an LLM API is unavailable:

Query

 ↓

Local retrieval

 ↓

Relevant rules

 ↓

Source-backed fallback answer

---

# Requirements

Python 3.10 or newer is recommended.

Install dependencies:

```bash
pip install -r requirements.txt