from langchain_core.prompts import ChatPromptTemplate 
from langchain.schema.runnable import RunnableLambda,RunnableParallel,RunnableBranch
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser 
import os 
from dotenv import load_dotenv
load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
model = ChatAnthropic(model="claude-3-opus-20240229")


messages1 = [
    ("system", "You are a developer helps to build code in the python given topic."),
    ("human","help me with the code {topic}"),
]

messages2 = [
    ("system", "You are a tester helps to determine weather the code is correct. If not mention word 'Wrong' and tell Reason in 2 lines along with code. If it is correct mention word 'Correct'."),
    ("human","help me with the code {code}"),
]

messages3=[
    ("system","You are a developer helps to fix the code given the reason and the code"),
    ("human","help me fix this {code}"),
]

messages4=[
    ("system","You are a satisfied developer with the answer from your junior"),
    ("human"," appreciate Him with the codefeed {code}"),
]

messages5=[
    ("system","say sorry to user for the code"),
     ("human","say sorry to user for the code {code}"),
]

m1=ChatPromptTemplate.from_messages(messages1)
m2=ChatPromptTemplate.from_messages(messages2)
m3=ChatPromptTemplate.from_messages(messages3)
m4=ChatPromptTemplate.from_messages(messages4)
m5=ChatPromptTemplate.from_messages(messages5)


branches = RunnableBranch(
    (
        lambda x: "correct" in x.lower(),
        m4|model|StrOutputParser() 
    ),
    (
        lambda x: "wrong" in x.lower(),
        m3 | model | StrOutputParser()  
    ),
    m5 | model | StrOutputParser()
)

cc = m2 | model | StrOutputParser()

chain = m1|llm|StrOutputParser()|cc|branches

print(chain.invoke({"topic": "Code to print 3 line height triangle inside a  5 radius circle with all stars"}))

