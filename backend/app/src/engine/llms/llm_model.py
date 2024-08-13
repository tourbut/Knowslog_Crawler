from langchain_openai import ChatOpenAI
from prompt import get_translate_prompt, get_summary_prompt

def translate_chain(api_key:str,
                    model:str='gpt-4o-mini',
                    temperature:float=0.7):
    prompt = get_translate_prompt()

    llm = ChatOpenAI(model=model,
                     temperature=temperature,
                     api_key=api_key)
    
    chain = prompt|llm
    return chain