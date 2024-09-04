from langchain.document_loaders import UnstructuredFileLoader

async def file_load(file_path: str):
    loader = UnstructuredFileLoader(file_path)