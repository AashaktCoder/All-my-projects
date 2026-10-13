import re


# ============================================================
# PDF + OCR EXTRACTION
# ============================================================

def extract_pdf(pdf_path):

    import pymupdf
    import pytesseract
    from PIL import Image

    document = pymupdf.open(pdf_path)

    pages = []

    for page_number, page in enumerate(
        document,
        start=1
    ):

        text = page.get_text("text").strip()

        # If page contains little/no text,
        # assume it may be scanned.
        if len(text) < 50:

            pixmap = page.get_pixmap(
                matrix=pymupdf.Matrix(2, 2),
                alpha=False
            )

            image = Image.frombytes(
                "RGB",
                [
                    pixmap.width,
                    pixmap.height
                ],
                pixmap.samples
            )

            text = pytesseract.image_to_string(
                image
            ).strip()

            source = "OCR"

        else:

            source = "PDF Text"

        pages.append(
            {
                "page": page_number,
                "text": text,
                "source": source
            }
        )

    document.close()

    return pages


# ============================================================
# RULE CLASSIFICATION
# ============================================================

def classify_rule(text):

    text_lower = text.lower()

    categories = {

        "rights": [
            "right",
            "entitled",
            "may request",
            "access",
            "appeal"
        ],

        "duties": [
            "must",
            "required",
            "responsible",
            "duty",
            "return"
        ],

        "restrictions": [
            "prohibited",
            "not permitted",
            "forbidden",
            "restricted",
            "must not"
        ],

        "procedures": [
            "procedure",
            "submit",
            "form",
            "register",
            "complaint",
            "within"
        ],

        "remedies": [
            "appeal",
            "remedy",
            "review",
            "escalate",
            "outcome"
        ]
    }

    scores = {}

    for category, keywords in categories.items():

        score = 0

        for keyword in keywords:

            if keyword in text_lower:
                score += 1

        scores[category] = score

    return max(
        scores,
        key=scores.get
    )


# ============================================================
# CHUNKING
# ============================================================

def chunk_pages(pages):

    chunks = []

    for page in pages:

        text = re.sub(
            r"\s+",
            " ",
            page["text"]
        ).strip()

        if not text:
            continue

        # Split around Section / Rule / Chapter headings.
        parts = re.split(
            r"(?=(?:Section|Rule|Chapter)\s+\d+)",
            text,
            flags=re.IGNORECASE
        )

        for part in parts:

            part = part.strip()

            if len(part) < 30:
                continue

            heading_match = re.search(
                r"((?:Section|Rule|Chapter)\s+[\w.-]+[^.:\n]*)",
                part,
                flags=re.IGNORECASE
            )

            if heading_match:

                section = heading_match.group(1).strip()

            else:

                section = (
                    f"Page {page['page']}"
                )

            chunks.append(
                {
                    "page": page["page"],
                    "section": section,
                    "category": classify_rule(part),
                    "text": part
                }
            )

    return chunks


# ============================================================
# COMPLETE PROCESSING PIPELINE
# ============================================================

def process_rulebook(
    db,
    rag,
    institution_id,
    pdf_path,
    version_label
):

    pages = extract_pdf(
        pdf_path
    )

    chunks = chunk_pages(
        pages
    )

    if not chunks:

        raise ValueError(
            "No readable text could be extracted from the rulebook."
        )

    version_id = db.add_version(
        institution_id,
        version_label,
        pdf_path
    )

    db.add_rules(
        institution_id,
        version_id,
        chunks
    )

    rag.rebuild(
        institution_id
    )

    return {
        "version_id": version_id,
        "pages": len(pages),
        "chunks": len(chunks)
    }