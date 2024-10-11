from langchain.prompts import PromptTemplate,ChatPromptTemplate,MessagesPlaceholder
from langchain.callbacks import StdOutCallbackHandler
from langchain.callbacks.manager import CallbackManager
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough,RunnableSequence,RunnableParallel
import os
from dotenv import load_dotenv
import langchain


strparser = StrOutputParser()

from pydantic import BaseModel, Field

class AIThink(BaseModel):
    THOUGHT: str = Field(..., title="모델이 생각하는 내용")

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

def get_thinking_prompt(pydantic_parser:PydanticOutputParser):
    template="""
<INSTRUCTION>
You are in the process of carefully considering the user's question or request. Your task is to think deeply about the user's input, analyze it from multiple perspectives, and consider all relevant factors before formulating your response.
First, ensure you fully understand the user's intent and the context of their question. Review the <CHAT_HISTORY> section to reference past interactions, and if necessary, summarize the relevant parts to better understand the user's needs and preferences.
Explore different possible interpretations and potential answers. Weigh the pros and cons of each option, and think about how your response will address the user's needs in the most effective way.
If the question is complex, break it down into manageable parts and analyze each part systematically. Consider any potential follow-up questions or concerns that might arise from your response.
Structure your response in a clear and organized manner, ensuring it follows a logical flow. Begin with a brief summary of the user's question, proceed with a detailed analysis, offer a well-considered recommendation, and conclude with a summary or invitation for further questions.
</INSTRUCTION>
<CHAT_HISTORY>
{chat_history}
</CHAT_HISTORY>
<INPUT>
{input}
</INPUT>
{format_instructions}

"""
    return PromptTemplate(
        template=template,
        input_variables=["chat_history", "input"],
        partial_variables={"format_instructions": pydantic_parser.get_format_instructions()}
    )
    
def get_thinking_chatbot():
    return ChatPromptTemplate.from_messages(
    [
        ("system", """
<INSTRUCTION>
You are an intelligent virtual assistant designed to help users.
Your interactions should always be friendly, empathetic, and clear.
When responding to user questions, you provide accurate and useful answers, taking the time to think through each question carefully and respond in a logical and systematic manner.
Always consider the <THOUGHT> section as a reflection of your reasoning process before finalizing your response. Use this to ensure that your answers are well-thought-out and effectively address the user's needs.

When necessary, you can offer additional relevant information.
While you can proactively guide or suggest ideas in the conversation, you must always respect the user's intent.
For complex questions, focus on explaining concepts in a simple and accessible way, avoiding jargon when possible.
Your goal is to maintain a positive and cooperative attitude, building trust with the user throughout the interaction.

As you interact with the user, continuously learn and adapt to their preferences, using previous conversations to offer more personalized and relevant responses in future interactions.

If you make a mistake or if the user seems confused or dissatisfied with your response, acknowledge it, apologize if necessary, and strive to provide the correct or clearer information.

Always adhere to ethical guidelines, especially regarding user privacy and sensitive topics. Never store, share, or misuse any personal or sensitive information provided by the user. Ensure that the user's data is handled with the highest level of confidentiality and respect.

</INSTRUCTION>

<THOUGHT>
{thought}
</THOUGHT>
"""),
        ("human", "{input}"),
    ]
    )
    
def create_llm():
    from langchain_openai import ChatOpenAI
    
    callback_manager = CallbackManager([StdOutCallbackHandler()])
    

    llm = ChatOpenAI(model='gpt-4o-mini',
                        temperature=0.7,
                        api_key=api_key,
                        callback_manager=callback_manager,
                        stream_usage=True)
    return llm

def create_chain():
    pydantic_parser = PydanticOutputParser(pydantic_object=AIThink)
    think_prompt = get_thinking_prompt(pydantic_parser)
    #print(think_prompt.invoke({"chat_history":"chain 개발중", "input":"내가 지금 뭘하고있지?"}))
    def get_thought(output):
        return output["thought"]
    
    def output_formatter(output):
        return {
            "thought": output["thought"],
            "answer": output["answer"]
        }
        
    prompt = get_thinking_chatbot()
    llm = create_llm()
    
    think_chain = think_prompt|llm|pydantic_parser
    answer_chain = prompt|llm
    final_chain = (
        think_chain
        |{
            "thought":RunnablePassthrough(),
            "input":RunnablePassthrough()
        }|
        {
            "thought":RunnableLambda(get_thought),
            "answer":answer_chain
        }|
        RunnableLambda(output_formatter)
        )
    
    return final_chain

def main():
    
    langchain.debug = False

    
    chain = create_chain()
        
    print('-' * 50,'START','-' * 50)
    chunks=[]
        
    for chunk in chain.stream({"chat_history":"chain 개발중", "input":"내가 지금 뭘하고있지?"}):
        print(chunk)
        chunks.append(chunk)
        
            
    #result = chain.invoke({"chat_history":"chain 개발중", "input":"내가 지금 뭘하고있지?"})
    
    print('-' * 51,'END','-' * 51)
    
    print(chunks)

def test():
    pydantic_parser = PydanticOutputParser(pydantic_object=AIThink)
    think_prompt = get_thinking_prompt(pydantic_parser)
    prompt = get_thinking_chatbot()
    #llm = create_llm()
    
    def test_llm(output):
        thought = "llm이 생각하는 내용 테스트중"
        return thought
    
    def get_thought(output):
        print(output)
        return output["thought"]
    
    def output_formatter(output):
        return {
            "thought": output["thought"],
            "answer": output["answer"]
        }
    
    
    think_chain = think_prompt|RunnableLambda(test_llm)
    answer_chain = prompt|RunnableLambda(lambda x: x)
    
    test_chat = RunnableParallel(
        thought = think_chain,
        input = RunnablePassthrough()
    )
    
    final_chain = (
        RunnableParallel(
            thought = think_chain,
            input = RunnablePassthrough()
        )|
        {
            "thought":RunnableLambda(get_thought),
            "answer":answer_chain
        }|
        RunnableLambda(output_formatter)
        )
    
    result = final_chain.invoke({"chat_history":"chain 개발중", "input":"내가 지금 뭘하고있지?"})
    
    print(result)
    
if __name__ == '__main__':
    test()