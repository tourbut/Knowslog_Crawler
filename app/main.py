from crawler import get_webpage, get_medium
from llms.llm_model import create_chain

if __name__ == "__main__":
    url ="https://arxiv.org/html/2405.12130v1"
    document = get_webpage(url=url)
    chain = create_chain()
    result = chain.invoke({"document":document})
    print("contents : ",result.content)
    print("-"*50)
    print("metadata : ",result.response_metadata)