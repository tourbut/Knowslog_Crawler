from langchain_openai import ChatOpenAI

def create_chain(prompt, parser=None):
    llm = ChatOpenAI(model = 'gpt-4o',temperature=0.5)
    chain = prompt|llm
    return chain