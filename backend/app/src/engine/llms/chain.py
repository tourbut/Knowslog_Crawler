from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.runnables.history import RunnableWithMessageHistory

from .prompt import get_translate_prompt, get_summary_prompt,get_chatbot_prompt,get_chatbot_prompt_with_history
from .parser import strparser

from langchain.globals import set_llm_cache
from langchain_community.cache import SQLiteCache, SQLAlchemyCache
#from ...deps import engine
#set_llm_cache(SQLAlchemyCache(engine))

set_llm_cache(SQLiteCache(database_path=".cache.db"))


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
                  callback_manager=None,
                  get_redis_history=None):
    
    prompt = get_chatbot_prompt_with_history()
    
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


    # Create a runnable with message history
    chain_with_history = RunnableWithMessageHistory(
    chain, get_redis_history, input_messages_key="input", history_messages_key="history"
    )
    
    return chain_with_history