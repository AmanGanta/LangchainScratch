from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
messages = [
    ("system", "You are a developer helps to finds error in the python code given topic for logic {topic}."),
    ("human","Here is the code {code}"),
]
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "sum of two numbers", "code": 'print(a*b)'})

print(llm.invoke(prompt))
print("\n\n Content : \n\n")
print(llm.invoke(prompt).content)