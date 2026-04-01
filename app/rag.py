import os

class RAGSystem:
    def __init__(self, knowledge_dir="knowledge"):
        self.knowledge_dir = knowledge_dir
        self.documents = self.load_documents()

    def load_documents(self):
        docs = []

        for file in os.listdir(self.knowledge_dir):
            if file.endswith(".md"):
                path = os.path.join(self.knowledge_dir, file)

                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()

                    docs.append({
                        "filename": file,
                        "content": content.lower()
                    })

        return docs

    def search(self, query: str):
        query = query.lower()
        results = []

        for doc in self.documents:
            content = doc["content"]

            if query in content:
                index = content.find(query)
                start = max(0, index - 100)
                end = index + 100

                snippet = content[start:end]

                results.append({
                    "filename": doc["filename"],
                    "snippet": snippet
                })

        return results