class Embedder:

    def __init__(self):

        self.model = None
        self.available = False
        self.error = None

    def load_model(self):

        if self.model is not None:
            return True

        try:

            from sentence_transformers import SentenceTransformer

            print("Loading Sentence Transformer model...")

            self.model = SentenceTransformer(
                "all-MiniLM-L6-v2"
            )

            self.available = True

            print("Sentence Transformer ready.")

            return True

        except Exception as e:

            self.available = False
            self.error = str(e)

            print(
                "Sentence Transformers unavailable."
            )

            print(e)

            return False

    def encode(self, texts):

        if not self.load_model():

            return None

        try:

            return self.model.encode(
                texts,
                normalize_embeddings=True
            )

        except Exception as e:

            print(
                "Embedding failed:",
                e
            )

            return None