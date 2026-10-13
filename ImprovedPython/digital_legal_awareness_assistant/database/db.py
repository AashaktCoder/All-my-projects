import os
import sqlite3


class Database:

    def __init__(self):
        self.conn = None
        self.mysql = False

        self.connect()

    # ---------------------------------------------------------
    # CONNECTION
    # ---------------------------------------------------------

    def connect(self):

        try:
            import mysql.connector

            host = os.getenv("MYSQL_HOST")
            user = os.getenv("MYSQL_USER")
            password = os.getenv("MYSQL_PASSWORD")
            database = os.getenv("MYSQL_DATABASE")

            if host and user and database:

                self.conn = mysql.connector.connect(
                    host=host,
                    port=int(os.getenv("MYSQL_PORT", "3306")),
                    user=user,
                    password=password,
                    database=database
                )

                self.mysql = True

                print("Connected to MySQL.")
                return

        except Exception as e:
            print("MySQL unavailable:", e)

        # -----------------------------------------------------
        # SQLITE FALLBACK
        # -----------------------------------------------------

        os.makedirs("data", exist_ok=True)

        self.conn = sqlite3.connect(
            "data/demo.db",
            check_same_thread=False
        )

        self.conn.row_factory = sqlite3.Row

        print("Using SQLite demo database.")

    # ---------------------------------------------------------
    # QUERY EXECUTION
    # ---------------------------------------------------------

    def execute(
        self,
        sql,
        params=(),
        fetch=False,
        many=False
    ):

        cursor = self.conn.cursor()

        if self.mysql:
            sql = sql.replace("?", "%s")

        if many:
            cursor.executemany(sql, params)

        else:
            cursor.execute(sql, params)

        if fetch:
            return cursor.fetchall()

        self.conn.commit()

        return cursor

    # ---------------------------------------------------------
    # INITIALIZE DATABASE
    # ---------------------------------------------------------

    def initialize(self):

        if self.mysql:

            queries = [

                """
                CREATE TABLE IF NOT EXISTS institutions (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    description TEXT,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
                """,

                """
                CREATE TABLE IF NOT EXISTS rulebook_versions (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    institution_id INT NOT NULL,
                    version_label VARCHAR(100) NOT NULL,
                    file_path TEXT,
                    uploaded_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    is_active BOOLEAN DEFAULT TRUE,

                    FOREIGN KEY(institution_id)
                    REFERENCES institutions(id)
                )
                """,

                """
                CREATE TABLE IF NOT EXISTS rules (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    institution_id INT NOT NULL,
                    version_id INT NOT NULL,
                    section VARCHAR(255),
                    page INT,
                    category VARCHAR(50),
                    text TEXT NOT NULL,

                    FOREIGN KEY(institution_id)
                    REFERENCES institutions(id),

                    FOREIGN KEY(version_id)
                    REFERENCES rulebook_versions(id)
                )
                """
            ]

        else:

            queries = [

                """
                CREATE TABLE IF NOT EXISTS institutions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP
                )
                """,

                """
                CREATE TABLE IF NOT EXISTS rulebook_versions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    institution_id INTEGER NOT NULL,
                    version_label TEXT NOT NULL,
                    file_path TEXT,
                    uploaded_at TEXT DEFAULT CURRENT_TIMESTAMP,
                    is_active INTEGER DEFAULT 1
                )
                """,

                """
                CREATE TABLE IF NOT EXISTS rules (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    institution_id INTEGER NOT NULL,
                    version_id INTEGER NOT NULL,
                    section TEXT,
                    page INTEGER,
                    category TEXT,
                    text TEXT NOT NULL
                )
                """
            ]

        for query in queries:
            self.execute(query)

    # ---------------------------------------------------------
    # DEMO DATA
    # ---------------------------------------------------------

    def seed_demo_data(self):

        existing = self.execute(
            """
            SELECT id
            FROM institutions
            WHERE name=?
            """,
            ("Sunrise Community Learning Centre",),
            fetch=True
        )

        if existing:
            return

        cursor = self.execute(
            """
            INSERT INTO institutions
            (name, description)
            VALUES (?, ?)
            """,
            (
                "Sunrise Community Learning Centre",
                "Fictional institution used for SIH demonstration."
            )
        )

        institution_id = cursor.lastrowid

        os.makedirs(
            "data/rulebooks",
            exist_ok=True
        )

        pdf_path = os.path.join(
            "data",
            "rulebooks",
            "sunrise_demo_rulebook.pdf"
        )

        self.create_demo_pdf(pdf_path)

        version_cursor = self.execute(
            """
            INSERT INTO rulebook_versions
            (
                institution_id,
                version_label,
                file_path,
                is_active
            )
            VALUES (?, ?, ?, 1)
            """,
            (
                institution_id,
                "v1.0 Demo",
                pdf_path
            )
        )

        version_id = version_cursor.lastrowid

        rules = [

            (
                "Section 1 - Member Rights",
                1,
                "rights",
                """
                Members have the right to access learning facilities
                during published opening hours.

                Members may request an explanation of a disciplinary
                decision.

                Members may submit an appeal against a disciplinary
                decision within 7 working days.
                """
            ),

            (
                "Section 2 - Member Duties",
                1,
                "duties",
                """
                Members must follow safety instructions.

                Members must respect staff and other members.

                Members must keep shared spaces reasonably clean.

                Members must return borrowed learning materials by
                the due date.
                """
            ),

            (
                "Section 3 - Restrictions",
                1,
                "restrictions",
                """
                Visitors must register at reception.

                Visitors must remain with an authorised host.

                Recording inside private counselling rooms is prohibited.

                Dangerous items are not permitted on the premises.

                Disruptive conduct is not permitted.
                """
            ),

            (
                "Section 4 - Complaints Procedure",
                2,
                "procedures",
                """
                A complaint should first be submitted to the Centre
                Coordinator using the complaint form.

                The Coordinator should acknowledge receipt within
                3 working days.

                If the complainant is dissatisfied, the matter may
                be escalated to the Review Committee.
                """
            ),

            (
                "Section 5 - Remedies and Appeals",
                2,
                "remedies",
                """
                A member who receives a disciplinary decision may
                request written reasons.

                A member may submit supporting information.

                A member may appeal to the Review Committee within
                7 working days.

                The Committee should provide an outcome within
                10 working days.
                """
            ),

            (
                "Section 6 - Library",
                2,
                "procedures",
                """
                The library is open Monday to Saturday from
                9:00 AM to 6:00 PM.

                Members may borrow up to three books.

                The borrowing period is fourteen days.

                Renewals may be requested before the due date.
                """
            )
        ]

        self.execute(
            """
            INSERT INTO rules
            (
                institution_id,
                version_id,
                section,
                page,
                category,
                text
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            [
                (
                    institution_id,
                    version_id,
                    section,
                    page,
                    category,
                    text
                )
                for section, page, category, text in rules
            ],
            many=True
        )

    # ---------------------------------------------------------
    # CREATE DEMO PDF
    # ---------------------------------------------------------

    def create_demo_pdf(self, path):

        try:

            import pymupdf

            document = pymupdf.open()

            page = document.new_page()

            page.insert_text(
                (50, 60),
                """
SUNRISE COMMUNITY LEARNING CENTRE
RULEBOOK v1.0


Section 1 - Member Rights

Members have the right to access learning facilities during
published opening hours.

Members may request an explanation of a disciplinary decision.

Members may submit an appeal against a disciplinary decision
within 7 working days.


Section 2 - Member Duties

Members must follow safety instructions.

Members must respect staff and other members.

Members must keep shared spaces reasonably clean.

Members must return borrowed learning materials by the due date.
""",
                fontsize=11
            )

            page = document.new_page()

            page.insert_text(
                (50, 60),
                """
SUNRISE COMMUNITY LEARNING CENTRE
RULEBOOK v1.0


Section 3 - Restrictions

Visitors must register at reception.

Visitors must remain with an authorised host.

Recording inside private counselling rooms is prohibited.

Dangerous items are not permitted on the premises.

Disruptive conduct is not permitted.


Section 4 - Complaints Procedure

A complaint should first be submitted to the Centre Coordinator
using the complaint form.

The Coordinator should acknowledge receipt within 3 working days.

If the complainant is dissatisfied, the matter may be escalated
to the Review Committee.


Section 5 - Remedies and Appeals

A member may request written reasons.

A member may submit supporting information.

A member may appeal to the Review Committee within 7 working days.

The Committee should provide an outcome within 10 working days.


Section 6 - Library

The library is open Monday to Saturday from 9:00 AM to 6:00 PM.

Members may borrow up to three books.

The borrowing period is fourteen days.
""",
                fontsize=11
            )

            document.save(path)
            document.close()

        except Exception as e:
            print("Could not create demo PDF:", e)

    # ---------------------------------------------------------
    # INSTITUTIONS
    # ---------------------------------------------------------

    def institutions(self):

        return self.execute(
            """
            SELECT *
            FROM institutions
            ORDER BY name
            """,
            fetch=True
        )

    def add_institution(
        self,
        name,
        description
    ):

        cursor = self.execute(
            """
            INSERT INTO institutions
            (name, description)
            VALUES (?, ?)
            """,
            (name, description)
        )

        return cursor.lastrowid

    # ---------------------------------------------------------
    # RULEBOOK VERSIONS
    # ---------------------------------------------------------

    def add_version(
        self,
        institution_id,
        version_label,
        file_path
    ):

        self.execute(
            """
            UPDATE rulebook_versions
            SET is_active=0
            WHERE institution_id=?
            """,
            (institution_id,)
        )

        cursor = self.execute(
            """
            INSERT INTO rulebook_versions
            (
                institution_id,
                version_label,
                file_path,
                is_active
            )
            VALUES (?, ?, ?, 1)
            """,
            (
                institution_id,
                version_label,
                file_path
            )
        )

        return cursor.lastrowid

    def versions(
        self,
        institution_id
    ):

        return self.execute(
            """
            SELECT *
            FROM rulebook_versions
            WHERE institution_id=?
            ORDER BY id DESC
            """,
            (institution_id,),
            fetch=True
        )

    def active_version(
        self,
        institution_id
    ):

        rows = self.execute(
            """
            SELECT *
            FROM rulebook_versions
            WHERE institution_id=?
            AND is_active=1
            ORDER BY id DESC
            LIMIT 1
            """,
            (institution_id,),
            fetch=True
        )

        return rows[0] if rows else None

    # ---------------------------------------------------------
    # RULES
    # ---------------------------------------------------------

    def add_rules(
        self,
        institution_id,
        version_id,
        chunks
    ):

        self.execute(
            """
            DELETE FROM rules
            WHERE version_id=?
            """,
            (version_id,)
        )

        data = []

        for chunk in chunks:

            data.append(
                (
                    institution_id,
                    version_id,
                    chunk["section"],
                    chunk["page"],
                    chunk["category"],
                    chunk["text"]
                )
            )

        self.execute(
            """
            INSERT INTO rules
            (
                institution_id,
                version_id,
                section,
                page,
                category,
                text
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            data,
            many=True
        )

    def rules_for_institution(
        self,
        institution_id
    ):

        version = self.active_version(
            institution_id
        )

        if not version:
            return []

        return self.execute(
            """
            SELECT *
            FROM rules
            WHERE institution_id=?
            AND version_id=?
            ORDER BY page, id
            """,
            (
                institution_id,
                version["id"]
            ),
            fetch=True
        )