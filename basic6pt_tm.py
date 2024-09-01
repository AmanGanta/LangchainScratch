from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
messages = [
    ("system", "You are a developer helps to finds error in the python code given topic for logic {topic}."),
    ("human","Here is the code {code}"),
]
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "sum of two numbers", "code": 'print(a*b)'})

print(prompt)