from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate 
from langchain.schema.runnable import RunnableLambda,RunnableParallel
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser 
import streamlit as st 
import os 
from dotenv import load_dotenv
load_dotenv()

model = ChatAnthropic(model="claude-3-opus-20240229")
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
llm2=ChatOpenAI(model="gpt-3.5-turbo")

messages = [
    ("system", "You are a developer helps to build code in the python given topic."),
    ("human","help me with the code {topic}"),
]
messages1 = [
    ("system", "You are a developer helps to Identify right and best code given two codes."),
    ("human","help me with the code {code}"),
]
def combine(goog, chg):
    return f"Code 1:\n{goog}\n\Code2:\n{chg}"

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt_template1 = ChatPromptTemplate.from_messages(messages1)
g_branch_chain=(RunnableLambda(lambda x: llm|StrOutputParser()))
c_branch_chain=(RunnableLambda(lambda x: llm2|StrOutputParser()))
chain = (
    prompt_template
    | RunnableParallel(branches={"goog": g_branch_chain, "chg": c_branch_chain})
    | RunnableLambda(lambda x: combine(x["branches"]["goog"], x["branches"]["chg"]))
    | prompt_template1
    | model
    |StrOutputParser()
)

print(chain.invoke({"topic": "Code to print 3 line height triangle inside a  5 radius circle with all stars"}))


