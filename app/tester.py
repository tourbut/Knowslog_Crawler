
from database.crud import create_user,create_archive,create_user_detail
from crawler import get_webpage, get_medium

from llms.llm_model import create_chain
from llms.prompt import get_translate_prompt, get_summary_prompt

if __name__ == "__main__":
    
    url="https://medium.com/cyberark-engineering/an-llm-journey-from-poc-to-production-6c5ec6a172fb"
    document = get_medium(url=url,txt_html=None)
    print(document)
    
    prompt = get_translate_prompt()
    chain = create_chain(prompt=prompt)
    result = chain.invoke({"document":document['contents']})
    print(result)
    
    create_archive(category="Medium",language="kr",
                   title=document['title'],
                   author=document['author'],
                   content=result.content,
                   url=document['url'])
    
    