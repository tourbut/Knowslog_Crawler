from crawler import get_webpage, get_medium
from llm_model import create_chain

if __name__ == "__main__":
    url ="https://medium.com/dev-genius/dockerize-your-llm-fastapi-project-%EF%B8%8F-7e4f872dff4f"
    medium = get_medium(url=url,txt_html=None)
    chain = create_chain()
    result = chain.invoke({"document":medium})
    print("contents : ",result.content)
    print("-"*50)
    print("metadata : ",result.response_metadata)