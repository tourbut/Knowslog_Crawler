from langchain.prompts import PromptTemplate

def get_chatbot_prompt():
    return PromptTemplate.from_template(
        template="""
<INSTRUCTION>
You are an intelligent virtual assistant designed to help users.
Your interactions should always be friendly, empathetic, and clear.
When responding to user questions, you provide accurate and useful answers, taking the time to think through each question carefully and respond in a logical and systematic manner.
When necessary, you can offer additional relevant information.
While you can proactively guide or suggest ideas in the conversation, you must always respect the user's intent.
For complex questions, focus on explaining concepts in a simple and accessible way, avoiding jargon when possible.
Your goal is to maintain a positive and cooperative attitude, building trust with the user throughout the interaction.
</INSTRUCTION>

<INPUT>
{input}
</INPUT>
"""
    )

def get_translate_prompt():
    return PromptTemplate.from_template(
        template="""
<INSTRUCTION>
Translate the text entered in <DOCUMENT> perfectly into Korean.
Be careful not to omit any content.
Keep the links within the document intact.
The final output format should be fixed in Markdown.
</INSTRUCTION>
<DOCUMENT>
{document}
</DOCUMENT> 
"""
    )

def get_summary_prompt():
    return PromptTemplate.from_template(
        template="""
<INSTRUCTION>
Rewrite the text entered in <DOCUMENT> in Korean according to the <OUTPUT FORMAT>.
The final output format should be fixed in Markdown.
Do not arbitrarily create content unrelated to the input text.
</INSTRUCTION>

<DOCUMENT>
{document}
</DOCUMENT>
<OUTPUT_FORMAT>
# (title)
출처 : [(title)-(author)]((url))

# TL;DR
- Write the content (approximately 1000 characters per item)

# Table of Contents
- Write the main contents as a table of contents

# (Section Name)
- If the original document contains image links, replace them with '![Image Name](Link Address)'
- Do not summarize program code content; include it as-is, translating any comments within the code into Korean.
- Make sure to include and emphasize all key points covered in the section.
</OUTPUT_FORMAT>
"""
    )