from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

from .prompt import get_translate_prompt, get_summary_prompt,get_chatbot_prompt
from .parser import strparser

from langchain.globals import set_llm_cache
from langchain_community.cache import SQLiteCache, SQLAlchemyCache
from ...deps import engine
#set_llm_cache(SQLiteCache(database_path=".langchain.db"))
set_llm_cache(SQLAlchemyCache(engine))


def translate_chain(api_key:str,
                    model:str='gpt-4o-mini',
                    temperature:float=0.7):
    
    prompt = get_translate_prompt()

    if model.startswith('gpt'):
        llm = ChatOpenAI(model=model,
                        temperature=temperature,
                        api_key=api_key)
    elif model.startswith('claude'):
        llm = ChatAnthropic(model=model,
                            temperature=temperature,
                            api_key=api_key)
    else:
        raise ValueError(f"Invalid model name: {model}")
    
    chain = prompt|llm
    return chain

def summarize_chain(api_key:str,
                    model:str='gpt-4o-mini',
                    temperature:float=0.7):
    
    prompt = get_summary_prompt()

    if model.startswith('gpt'):
        llm = ChatOpenAI(model=model,
                        temperature=temperature,
                        api_key=api_key)
    elif model.startswith('claude'):
        llm = ChatAnthropic(model=model,
                            temperature=temperature,
                            api_key=api_key)
    else:
        raise ValueError(f"Invalid model name: {model}")
    
    chain = prompt|llm
    return chain


def chatbot_chain(api_key:str,
                  model:str='gpt-4o-mini',
                  temperature:float=0.7,
                  callback_manager=None):
    
    prompt = get_chatbot_prompt()
    
    if model.startswith('gpt'):
        llm = ChatOpenAI(model=model,
                        temperature=temperature,
                        api_key=api_key,
                        callback_manager=callback_manager,
                        stream_usage=True)
        
    elif model.startswith('claude'):
        llm = ChatAnthropic(model=model,
                            temperature=temperature,
                            api_key=api_key,
                            callback_manager=callback_manager)
    else:
        raise ValueError(f"Invalid model name: {model}")
    
    chain = prompt|llm
    return chain