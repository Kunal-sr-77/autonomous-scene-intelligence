from pathlib import Path


class VectorStore:

    def __init__(self, kb_path="data/knowledge_base/traffic_rules.txt"):
        self.kb_path = kb_path
        self.documents = self.load_documents()

    def load_documents(self):

        path = Path(self.kb_path)

        with open(path, "r") as f:
            docs = f.readlines()

        return [doc.strip() for doc in docs if doc.strip()] 