import os
import re

from .embeddings import Embedder


class RAGEngine:

    def __init__(
        self,
        db
    ):

        self.db = db

        self.embedder = Embedder()

        self.indexes = {}

        try:

            import faiss

            self.faiss = faiss

            print(
                "FAISS enabled."
            )

        except Exception as e:

            self.faiss = None

            print(
                "FAISS unavailable:",
                e
            )

    # ========================================================
    # BUILD INDEX
    # ========================================================

    def rebuild(
        self,
        institution_id
    ):

        rules = [
            dict(row)
            for row in self.db.rules_for_institution(
                institution_id
            )
        ]

        if not rules:

            self.indexes.pop(
                institution_id,
                None
            )

            return

        texts = [
            rule["text"]
            for rule in rules
        ]

        vectors = self.embedder.encode(
            texts
        )

        if (
            vectors is not None
            and self.faiss is not None
        ):

            index = self.faiss.IndexFlatIP(
                vectors.shape[1]
            )

            index.add(
                vectors
            )

            self.indexes[
                institution_id
            ] = (
                index,
                rules
            )

        else:

            # Local keyword fallback.
            self.indexes[
                institution_id
            ] = (
                None,
                rules
            )

    # ========================================================
    # RETRIEVAL
    # ========================================================

    def retrieve(
        self,
        institution_id,
        query,
        k=4
    ):

        if institution_id not in self.indexes:

            self.rebuild(
                institution_id
            )

        data = self.indexes.get(
            institution_id
        )

        if not data:
            return []

        index, rules = data

        # ----------------------------------------------------
        # FAISS SEMANTIC SEARCH
        # ----------------------------------------------------

        if index is not None:

            query_vector = self.embedder.encode(
                [query]
            )

            scores, ids = index.search(
                query_vector,
                min(k, len(rules))
            )

            results = []

            for position, rule_id in enumerate(
                ids[0]
            ):

                if rule_id < 0:
                    continue

                results.append(
                    (
                        rules[rule_id],
                        float(
                            scores[0][position]
                        )
                    )
                )

            return results

        # ----------------------------------------------------
        # LOCAL FALLBACK
        # ----------------------------------------------------

        return self.keyword_retrieval(
            query,
            rules,
            k
        )

    # ========================================================
    # KEYWORD FALLBACK
    # ========================================================

    def keyword_retrieval(
        self,
        query,
        rules,
        k=4
    ):

        query_words = set(
            re.findall(
                r"[a-zA-Z0-9]+",
                query.lower()
            )
        )

        scored = []

        important_terms = [
            "appeal",
            "complaint",
            "library",
            "visitor",
            "duty",
            "right",
            "restriction",
            "prohibited",
            "procedure",
            "remedy",
            "disciplinary"
        ]

        for rule in rules:

            rule_words = set(
                re.findall(
                    r"[a-zA-Z0-9]+",
                    rule["text"].lower()
                )
            )

            overlap = len(
                query_words & rule_words
            )

            bonus = 0

            query_lower = query.lower()

            rule_lower = rule["text"].lower()

            for term in important_terms:

                if (
                    term in query_lower
                    and term in rule_lower
                ):

                    bonus += 2

            score = overlap + bonus

            scored.append(
                (
                    rule,
                    score
                )
            )

        scored.sort(
            key=lambda item: item[1],
            reverse=True
        )

        return scored[:k]

    # ========================================================
    # RAG ANSWER
    # ========================================================

    def answer(
        self,
        institution_id,
        query
    ):

        retrieved = self.retrieve(
            institution_id,
            query,
            4
        )

        if not retrieved:

            return {
                "answer":
                    "I could not find a relevant rule in "
                    "the selected institution's active rulebook.",

                "sources": []
            }

        context_parts = []

        for rule, score in retrieved:

            context_parts.append(
                f"""
SOURCE:
Section: {rule['section']}
Page: {rule['page']}
Category: {rule['category']}

RULE:
{rule['text']}
"""
            )

        context = "\n".join(
            context_parts
        )

        # ----------------------------------------------------
        # TRY LLM
        # ----------------------------------------------------

        llm_answer = self.call_llm(
            query,
            context
        )

        if llm_answer:

            final_answer = llm_answer

        else:

            final_answer = self.local_answer(
                query,
                retrieved
            )

        sources = []

        for rule, score in retrieved:

            sources.append(
                {
                    "section": rule["section"],
                    "page": rule["page"],
                    "category": rule["category"],
                    "score": round(
                        score,
                        3
                    )
                }
            )

        return {
            "answer": final_answer,
            "sources": sources
        }

    # ========================================================
    # LLM
    # ========================================================

    def call_llm(
        self,
        query,
        context
    ):

        api_key = os.getenv(
            "LLM_API_KEY"
        )

        if not api_key:
            return None

        try:

            import requests

            base_url = os.getenv(
                "LLM_BASE_URL",
                "https://api.openai.com/v1"
            ).rstrip("/")

            model = os.getenv(
                "LLM_MODEL",
                "gpt-4o-mini"
            )

            system_prompt = """
You are a Digital Legal Awareness Assistant.

Your task is to answer questions using ONLY the
provided institutional rulebook context.

Rules:

1. Never invent institutional rules.
2. Do not fabricate legal provisions.
3. Clearly distinguish institutional rules from general law.
4. If the supplied context does not answer the question,
   say that the rulebook does not provide enough information.
5. Give concise and understandable answers.
6. Mention relevant procedures or remedies when present.
7. Do not claim to be a lawyer.
"""

            payload = {

                "model": model,

                "messages": [

                    {
                        "role": "system",
                        "content": system_prompt
                    },

                    {
                        "role": "user",
                        "content":
                            f"""
RULEBOOK CONTEXT:

{context}

USER QUESTION:

{query}

Answer strictly from the supplied context.
"""
                    }

                ],

                "temperature": 0.1
            }

            response = requests.post(
                f"{base_url}/chat/completions",
                headers={
                    "Authorization":
                        f"Bearer {api_key}",

                    "Content-Type":
                        "application/json"
                },
                json=payload,
                timeout=30
            )

            response.raise_for_status()

            data = response.json()

            return (
                data["choices"][0]
                ["message"]
                ["content"]
                .strip()
            )

        except Exception as e:

            print(
                "LLM unavailable:",
                e
            )

            return None

    # ========================================================
    # LOCAL RAG FALLBACK
    # ========================================================

    def local_answer(
        self,
        query,
        retrieved
    ):

        if not retrieved:

            return (
                "No relevant rule was found."
            )

        best_rule = retrieved[0][0]

        answer = (
            "Based on the active rulebook:\n\n"
            f"{best_rule['text']}\n\n"
            f"Source: {best_rule['section']}, "
            f"page {best_rule['page']}."
        )

        return answer