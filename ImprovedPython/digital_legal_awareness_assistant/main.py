import os
import tkinter as tk

from database.db import Database
from document_processing.processor import process_rulebook
from ai.rag import RAGEngine
from ui.app import LegalAssistantApp


def main():
    os.makedirs("data", exist_ok=True)
    os.makedirs("data/rulebooks", exist_ok=True)
    os.makedirs("data/indexes", exist_ok=True)

    # Database automatically uses MySQL when configured,
    # otherwise SQLite is used for demo mode.
    db = Database()
    db.initialize()

    # Create fictional demo institution/rules.
    db.seed_demo_data()

    rag = RAGEngine(db)

    root = tk.Tk()

    app = LegalAssistantApp(
        root=root,
        db=db,
        rag=rag,
        process_callback=lambda institution_id, pdf_path, version_label:
            process_rulebook(
                db,
                rag,
                institution_id,
                pdf_path,
                version_label
            )
    )

    root.mainloop()


if __name__ == "__main__":
    main()