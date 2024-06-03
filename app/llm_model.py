from langchain.prompts import PromptTemplate,ChatPromptTemplate
from langchain_openai import ChatOpenAI

def get_summary_prompt():
    return PromptTemplate.from_template(
        template="""
<INSTRUCTION>
<DOCUMENT> 에 입력된 텍스트를 <출력양식>에 맞게 한국어로 재작성 하시오.
최종 출력 포맷은 Markdown으로 고정합니다.
입력된 텍스트와 관련이 없는 내용을 임의로 생성하지 마십시오.
</INSTRUCTION>

<DOCUMENT>
{document}
</DOCUMENT>
<출력양식>
# (title)
출처 : [(title)-(author)]((url))

# TL;DR
- 내용 작성(항목당 1000자 내외로 작성)

# 목차
- 주요 내용 목차로 작성

# (섹션명)
- 원본 문서에 이미지 링크가 있는 경우 해당 이미지 링크를 '![이미지명](링크주소)'로 변경하여 삽입
- 프로그램 코드 내용은 요약하지 않고 작성, 코드안에 주석이 있는 경우 한국어로 번역하여 작성.
- 섹션에서 다루고있는 주요한 요점들은 빠짐없이 작성 및 강조 표시.
</출력양식>
"""
    )
    
def create_chain():
    prompt = get_summary_prompt()
    llm = ChatOpenAI(model = 'gpt-4o',temperature=0.5)
    chain = prompt|llm
    return chain