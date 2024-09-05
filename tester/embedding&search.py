
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import CharacterTextSplitter, TokenTextSplitter
from langchain.embeddings import CacheBackedEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_postgres.vectorstores import PGVector
from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel import Session,create_engine


def load_and_split(file_path: str):
    character_text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    separator="\n",
    chunk_size=600,
    chunk_overlap=100,
    )
        
    loader = UnstructuredFileLoader(file_path)
    docs = loader.load_and_split(text_splitter=character_text_splitter)
    return docs

def embedding_and_store(docs, connection, collection_name:str, api_key:str, model:str='text-embedding-3-large'):
    embeddings = OpenAIEmbeddings(model=model,
                                  api_key=api_key)
    
    if type(connection) is Engine:
        async_mode=False
    elif type(connection) is AsyncEngine:
        async_mode=True
    else:
        raise ValueError("connection must be either Engine or AsyncEngine")
        
    vectorstore = PGVector(
    embeddings=embeddings,
    collection_name=collection_name,
    connection=connection,
    use_jsonb=True,
    async_mode=async_mode,
    )
    
    
    vectorstore.add_documents(documents=docs)
    
    return vectorstore

"""
파일 임베딩 및 검색 테스트
1. 파일 로드
2. 텍스트 분할
3. 임베딩
4. 백터 저장

"""

if __name__ == '__main__':
    
    collection_name = 'test_pdf'
    api_key=''
    url = ''
    
    engine = create_engine(url)
    
    docs = load_and_split('tester/test.txt')
    print(docs)
    
    vectorstore = embedding_and_store(docs, 
                                      connection=engine, 
                                      collection_name=collection_name, 
                                      api_key=api_key,
                                      model='text-embedding-3-large')
    
    print(vectorstore)
    