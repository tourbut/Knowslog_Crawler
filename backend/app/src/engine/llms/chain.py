from langchain_openai import ChatOpenAI
from .prompt import get_translate_prompt, get_summary_prompt
from .parser import strparser

from langchain.globals import set_llm_cache
from langchain_community.cache import SQLiteCache

set_llm_cache(SQLiteCache(database_path=".langchain.db"))

def translate_chain(api_key:str,
                    model:str='gpt-4o-mini',
                    temperature:float=0.7):
    
    prompt = get_translate_prompt()

    llm = ChatOpenAI(model=model,
                     temperature=temperature,
                     api_key=api_key)
    
    chain = prompt|llm
    return chain

def summarize_chain(api_key:str,
                    model:str='gpt-4o-mini',
                    temperature:float=0.7):
    
    prompt = get_summary_prompt()

    llm = ChatOpenAI(model=model,
                     temperature=temperature,
                     api_key=api_key)
    
    chain = prompt|llm
    return chain