from rag.vector_store import VectorStore


class Retriever:

    def __init__(self):
        self.store = VectorStore()

        # map scene objects to rule keywords
        self.keyword_map = {
            "person": ["person", "pedestrian", "people", "human"],
            "car": ["car", "vehicle"],
            "truck": ["truck", "vehicle"],
            "bus": ["bus", "vehicle"]
        }

    def retrieve(self, scene):

        objects = scene["objects"]

        relevant_docs = []

        for doc in self.store.documents:

            doc_lower = doc.lower()

            for obj in objects:

                keywords = self.keyword_map.get(obj, [obj])

                for word in keywords:

                    if word in doc_lower:
                        relevant_docs.append(doc)
                        break

        return relevant_docs[:3]