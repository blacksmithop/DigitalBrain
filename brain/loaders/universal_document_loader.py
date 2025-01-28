from langchain_unstructured import UnstructuredLoader


class UniversalDocumentLoader:
    def __init__(self):
        pass

    def load_document(self, file_path: str):
        loader = UnstructuredLoader(file_path=file_path)
        docs = loader.load()