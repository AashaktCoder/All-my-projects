import os
import shutil
import tkinter as tk

from tkinter import (
    ttk,
    filedialog,
    messagebox
)

from tkinter.scrolledtext import ScrolledText

from kyr.dashboard import (
    build_kyr
)


class LegalAssistantApp:

    def __init__(
        self,
        root,
        db,
        rag,
        process_callback
    ):

        self.root = root
        self.db = db
        self.rag = rag
        self.process_callback = process_callback

        self.root.title(
            "Digital Legal Awareness Assistant"
        )

        self.root.geometry(
            "1200x760"
        )

        self.root.minsize(
            1000,
            650
        )

        self.selected_institution = None

        self.setup_style()

        self.build_interface()

    # ========================================================
    # STYLE
    # ========================================================

    def setup_style(self):

        style = ttk.Style()

        try:
            style.theme_use(
                "clam"
            )
        except Exception:
            pass

        style.configure(
            "Title.TLabel",
            font=(
                "Segoe UI",
                20,
                "bold"
            )
        )

        style.configure(
            "Heading.TLabel",
            font=(
                "Segoe UI",
                12,
                "bold"
            )
        )

        style.configure(
            "Accent.TButton",
            font=(
                "Segoe UI",
                10,
                "bold"
            )
        )

    # ========================================================
    # MAIN INTERFACE
    # ========================================================

    def build_interface(self):

        # ----------------------------------------------------
        # HEADER
        # ----------------------------------------------------

        header = ttk.Frame(
            self.root,
            padding=18
        )

        header.pack(
            fill="x"
        )

        ttk.Label(
            header,
            text="DIGITAL LEGAL AWARENESS ASSISTANT",
            style="Title.TLabel"
        ).pack(
            side="left"
        )

        ttk.Label(
            header,
            text="  |  Know Your Rights Framework"
        ).pack(
            side="left",
            padx=10
        )

        self.mode_label = ttk.Label(
            header,
            text="● DEMO / LOCAL RAG"
        )

        self.mode_label.pack(
            side="right"
        )

        # ----------------------------------------------------
        # NOTEBOOK
        # ----------------------------------------------------

        notebook = ttk.Notebook(
            self.root
        )

        notebook.pack(
            fill="both",
            expand=True,
            padx=12,
            pady=(0, 12)
        )

        # ----------------------------------------------------
        # CREATE ALL TABS FIRST
        # ----------------------------------------------------

        self.user_tab = ttk.Frame(
            notebook,
            padding=15
        )

        self.kyr_tab = ttk.Frame(
            notebook,
            padding=15
        )

        self.admin_tab = ttk.Frame(
            notebook,
            padding=15
        )

        notebook.add(
            self.user_tab,
            text="  Ask Assistant  "
        )

        notebook.add(
            self.kyr_tab,
            text="  KYR Dashboard  "
        )

        notebook.add(
            self.admin_tab,
            text="  Admin Panel  "
        )

        # ----------------------------------------------------
        # BUILD WIDGETS
        # ----------------------------------------------------

        # IMPORTANT:
        # Admin is built first because refresh_institutions()
        # accesses admin_institution_combo.

        self.build_admin_tab()

        # Build KYR before anything can call refresh_kyr()

        self.build_kyr_tab()

        # Build user tab last because it calls
        # refresh_institutions()

        self.build_user_tab()

    # ========================================================
    # USER TAB
    # ========================================================

    def build_user_tab(self):

        institution_bar = ttk.Frame(
            self.user_tab
        )

        institution_bar.pack(
            fill="x"
        )

        ttk.Label(
            institution_bar,
            text="Institution:"
        ).pack(
            side="left"
        )

        self.institution_combo = ttk.Combobox(
            institution_bar,
            state="readonly",
            width=55
        )

        self.institution_combo.pack(
            side="left",
            padx=10
        )

        self.institution_combo.bind(
            "<<ComboboxSelected>>",
            lambda event:
                self.institution_changed()
        )

        ttk.Label(
            self.user_tab,
            text="Ask a natural-language question",
            style="Heading.TLabel"
        ).pack(
            anchor="w",
            pady=(20, 6)
        )

        self.question_box = tk.Text(
            self.user_tab,
            height=4,
            font=(
                "Segoe UI",
                11
            ),
            wrap="word"
        )

        self.question_box.pack(
            fill="x"
        )

        ttk.Button(
            self.user_tab,
            text="ASK ASSISTANT  →",
            style="Accent.TButton",
            command=self.ask_question
        ).pack(
            anchor="e",
            pady=10
        )

        # ----------------------------------------------------
        # RESPONSE / SOURCE AREA
        # ----------------------------------------------------

        paned = ttk.Panedwindow(
            self.user_tab,
            orient="horizontal"
        )

        paned.pack(
            fill="both",
            expand=True
        )

        response_frame = ttk.Frame(
            paned,
            padding=8
        )

        source_frame = ttk.Frame(
            paned,
            padding=8
        )

        paned.add(
            response_frame,
            weight=3
        )

        paned.add(
            source_frame,
            weight=2
        )

        ttk.Label(
            response_frame,
            text="AI RESPONSE",
            style="Heading.TLabel"
        ).pack(
            anchor="w"
        )

        self.answer_box = ScrolledText(
            response_frame,
            wrap="word",
            font=(
                "Segoe UI",
                11
            ),
            state="disabled"
        )

        self.answer_box.pack(
            fill="both",
            expand=True,
            pady=(5, 0)
        )

        ttk.Label(
            source_frame,
            text="SOURCE REFERENCES",
            style="Heading.TLabel"
        ).pack(
            anchor="w"
        )

        self.source_box = ScrolledText(
            source_frame,
            wrap="word",
            font=(
                "Segoe UI",
                10
            ),
            state="disabled"
        )

        self.source_box.pack(
            fill="both",
            expand=True,
            pady=(5, 0)
        )

        self.refresh_institutions()

    # ========================================================
    # KYR TAB
    # ========================================================

    def build_kyr_tab(self):

        ttk.Label(
            self.kyr_tab,
            text="KNOW YOUR RULES",
            style="Title.TLabel"
        ).pack(
            anchor="w"
        )

        ttk.Label(
            self.kyr_tab,
            text=(
                "Structured view of the active institutional rulebook."
            )
        ).pack(
            anchor="w",
            pady=(0, 15)
        )

        self.kyr_container = ttk.Frame(
            self.kyr_tab
        )

        self.kyr_container.pack(
            fill="both",
            expand=True
        )

    # ========================================================
    # ADMIN TAB
    # ========================================================

    def build_admin_tab(self):

        ttk.Label(
            self.admin_tab,
            text="ADMINISTRATION",
            style="Title.TLabel"
        ).pack(
            anchor="w"
        )

        # ----------------------------------------------------
        # ADD INSTITUTION
        # ----------------------------------------------------

        institution_frame = ttk.LabelFrame(
            self.admin_tab,
            text="Add Institution",
            padding=15
        )

        institution_frame.pack(
            fill="x",
            pady=10
        )

        ttk.Label(
            institution_frame,
            text="Institution name:"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=5
        )

        self.new_institution_name = ttk.Entry(
            institution_frame,
            width=60
        )

        self.new_institution_name.grid(
            row=0,
            column=1,
            padx=10
        )

        ttk.Label(
            institution_frame,
            text="Description:"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=5
        )

        self.new_institution_description = ttk.Entry(
            institution_frame,
            width=60
        )

        self.new_institution_description.grid(
            row=1,
            column=1,
            padx=10
        )

        ttk.Button(
            institution_frame,
            text="ADD INSTITUTION",
            command=self.add_institution
        ).grid(
            row=2,
            column=1,
            sticky="e",
            pady=10
        )

        # ----------------------------------------------------
        # RULEBOOK
        # ----------------------------------------------------

        rulebook_frame = ttk.LabelFrame(
            self.admin_tab,
            text="Rulebook Versioning & Processing",
            padding=15
        )

        rulebook_frame.pack(
            fill="x",
            pady=10
        )

        ttk.Label(
            rulebook_frame,
            text="Institution:"
        ).grid(
            row=0,
            column=0,
            sticky="w"
        )

        self.admin_institution_combo = ttk.Combobox(
            rulebook_frame,
            state="readonly",
            width=55
        )

        self.admin_institution_combo.grid(
            row=0,
            column=1,
            padx=10,
            pady=5
        )

        ttk.Label(
            rulebook_frame,
            text="Version:"
        ).grid(
            row=1,
            column=0,
            sticky="w"
        )

        self.version_entry = ttk.Entry(
            rulebook_frame,
            width=25
        )

        self.version_entry.insert(
            0,
            "v2.0"
        )

        self.version_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=5,
            sticky="w"
        )

        ttk.Button(
            rulebook_frame,
            text="UPLOAD / PROCESS RULEBOOK",
            command=self.upload_rulebook
        ).grid(
            row=2,
            column=1,
            sticky="e",
            pady=10
        )

        self.status_label = ttk.Label(
            self.admin_tab,
            text="System ready."
        )

        self.status_label.pack(
            anchor="w",
            pady=5
        )

        ttk.Label(
            self.admin_tab,
            text="RULEBOOK VERSION HISTORY",
            style="Heading.TLabel"
        ).pack(
            anchor="w",
            pady=(10, 5)
        )

        self.version_box = ScrolledText(
            self.admin_tab,
            height=10,
            wrap="word",
            state="disabled"
        )

        self.version_box.pack(
            fill="both",
            expand=True
        )

        self.admin_institution_combo.bind(
            "<<ComboboxSelected>>",
            lambda event:
                self.refresh_versions()
        )

    # ========================================================
    # INSTITUTIONS
    # ========================================================

    def refresh_institutions(self):

        rows = self.db.institutions()

        names = [
            row["name"]
            for row in rows
        ]

        self.institution_combo["values"] = names

        self.admin_institution_combo[
            "values"
        ] = names

        if names:

            if self.institution_combo.current() < 0:

                self.institution_combo.current(
                    0
                )

            if self.admin_institution_combo.current() < 0:

                self.admin_institution_combo.current(
                    0
                )

            self.institution_changed()

            self.refresh_versions()

    def institution_changed(self):

        name = self.institution_combo.get()

        institutions = self.db.institutions()

        institution = next(
            (
                row
                for row in institutions
                if row["name"] == name
            ),
            None
        )

        if institution:

            self.selected_institution = (
                institution["id"]
            )

            self.rag.rebuild(
                self.selected_institution
            )

        else:

            self.selected_institution = None

        self.refresh_kyr()

    # ========================================================
    # ADD INSTITUTION
    # ========================================================

    def add_institution(self):

        name = (
            self.new_institution_name
            .get()
            .strip()
        )

        description = (
            self.new_institution_description
            .get()
            .strip()
        )

        if not name:

            messagebox.showwarning(
                "Missing information",
                "Please enter an institution name."
            )

            return

        self.db.add_institution(
            name,
            description
        )

        self.new_institution_name.delete(
            0,
            "end"
        )

        self.new_institution_description.delete(
            0,
            "end"
        )

        self.refresh_institutions()

        messagebox.showinfo(
            "Success",
            "Institution added successfully."
        )

    # ========================================================
    # UPLOAD RULEBOOK
    # ========================================================

    def upload_rulebook(self):

        institution_name = (
            self.admin_institution_combo
            .get()
        )

        if not institution_name:

            messagebox.showwarning(
                "Institution",
                "Please select an institution."
            )

            return

        institutions = self.db.institutions()

        institution = next(
            (
                row
                for row in institutions
                if row["name"] == institution_name
            ),
            None
        )

        if not institution:
            return

        pdf_path = filedialog.askopenfilename(
            title="Select Rulebook PDF",
            filetypes=[
                (
                    "PDF files",
                    "*.pdf"
                )
            ]
        )

        if not pdf_path:
            return

        os.makedirs(
            "data/rulebooks",
            exist_ok=True
        )

        destination = os.path.join(
            "data",
            "rulebooks",
            os.path.basename(pdf_path)
        )

        if (
            os.path.abspath(pdf_path)
            != os.path.abspath(destination)
        ):

            shutil.copy2(
                pdf_path,
                destination
            )

        version_label = (
            self.version_entry
            .get()
            .strip()
        )

        if not version_label:

            version_label = "New Version"

        self.status_label.config(
            text="Processing PDF / OCR / RAG index..."
        )

        self.root.update_idletasks()

        try:

            result = self.process_callback(
                institution["id"],
                destination,
                version_label
            )

            self.status_label.config(
                text=(
                    f"Processed {result['pages']} pages | "
                    f"{result['chunks']} rules | "
                    "RAG index updated."
                )
            )

            self.refresh_versions()

            self.refresh_kyr()

            self.rag.rebuild(
                institution["id"]
            )

            messagebox.showinfo(
                "Processing complete",
                (
                    "Rulebook successfully processed.\n\n"
                    f"Pages: {result['pages']}\n"
                    f"Rules: {result['chunks']}\n\n"
                    "The new version is now active."
                )
            )

        except Exception as error:

            self.status_label.config(
                text="Processing failed."
            )

            messagebox.showerror(
                "Processing error",
                str(error)
            )

    # ========================================================
    # VERSION HISTORY
    # ========================================================

    def refresh_versions(self):

        institution_name = (
            self.admin_institution_combo
            .get()
        )

        if not institution_name:
            return

        institutions = self.db.institutions()

        institution = next(
            (
                row
                for row in institutions
                if row["name"] == institution_name
            ),
            None
        )

        if not institution:
            return

        versions = self.db.versions(
            institution["id"]
        )

        self.version_box.config(
            state="normal"
        )

        self.version_box.delete(
            "1.0",
            "end"
        )

        if not versions:

            self.version_box.insert(
                "end",
                "No rulebook versions available."
            )

        for version in versions:

            status = (
                "ACTIVE"
                if version["is_active"]
                else "ARCHIVED"
            )

            self.version_box.insert(
                "end",
                f"Version: {version['version_label']}\n"
                f"Status: {status}\n"
                f"File: {version['file_path']}\n"
                f"Uploaded: {version['uploaded_at']}\n"
                f"{'-' * 60}\n"
            )

        self.version_box.config(
            state="disabled"
        )

    # ========================================================
    # KYR DASHBOARD
    # ========================================================

    def refresh_kyr(self):

        for widget in (
            self.kyr_container
            .winfo_children()
        ):

            widget.destroy()

        if not self.selected_institution:

            return

        rules = self.db.rules_for_institution(
            self.selected_institution
        )

        groups = build_kyr(
            rules
        )

        columns = [

            ("RIGHTS", "rights"),

            ("DUTIES", "duties"),

            ("RESTRICTIONS", "restrictions"),

            ("PROCEDURES", "procedures"),

            ("REMEDIES", "remedies")
        ]

        for column, (
            title,
            category
        ) in enumerate(columns):

            self.kyr_container.columnconfigure(
                column,
                weight=1
            )

            frame = ttk.LabelFrame(
                self.kyr_container,
                text=title,
                padding=8
            )

            frame.grid(
                row=0,
                column=column,
                padx=5,
                sticky="nsew"
            )

            text = ScrolledText(
                frame,
                width=24,
                height=24,
                wrap="word",
                font=(
                    "Segoe UI",
                    9
                )
            )

            text.pack(
                fill="both",
                expand=True
            )

            category_rules = groups[
                category
            ]

            if not category_rules:

                text.insert(
                    "end",
                    "No rules found."
                )

            for rule in category_rules:

                text.insert(
                    "end",
                    f"• {rule['text']}\n\n"
                )

            text.config(
                state="disabled"
            )

    # ========================================================
    # ASK QUESTION
    # ========================================================

    def ask_question(self):

        if not self.selected_institution:

            messagebox.showwarning(
                "Institution",
                "Please select an institution."
            )

            return

        question = (
            self.question_box
            .get(
                "1.0",
                "end"
            )
            .strip()
        )

        if not question:
            return

        self.answer_box.config(
            state="normal"
        )

        self.answer_box.delete(
            "1.0",
            "end"
        )

        self.answer_box.insert(
            "end",
            "Retrieving relevant rules..."
        )

        self.answer_box.config(
            state="disabled"
        )

        self.root.update_idletasks()

        result = self.rag.answer(
            self.selected_institution,
            question
        )

        # ----------------------------------------------------
        # ANSWER
        # ----------------------------------------------------

        self.answer_box.config(
            state="normal"
        )

        self.answer_box.delete(
            "1.0",
            "end"
        )

        self.answer_box.insert(
            "end",
            result["answer"]
        )

        self.answer_box.config(
            state="disabled"
        )

        # ----------------------------------------------------
        # SOURCES
        # ----------------------------------------------------

        self.source_box.config(
            state="normal"
        )

        self.source_box.delete(
            "1.0",
            "end"
        )

        if not result["sources"]:

            self.source_box.insert(
                "end",
                "No source found."
            )

        else:

            for index, source in enumerate(
                result["sources"],
                start=1
            ):

                self.source_box.insert(
                    "end",
                    (
                        f"SOURCE {index}\n"
                        f"Section: {source['section']}\n"
                        f"Page: {source['page']}\n"
                        f"Category: {source['category']}\n"
                        f"Retrieval score: {source['score']}\n\n"
                    )
                )

        self.source_box.config(
            state="disabled"
        )