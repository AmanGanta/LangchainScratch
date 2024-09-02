#USING OPENAI FOR building chaT BOT 
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate 
from langchain.schema.runnable import RunnableLambda
from langchain_core.output_parsers import StrOutputParser 
import streamlit as st 
import os 
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"


prompt = ChatPromptTemplate.from_messages([
    ('system', "please assist the user based on his needs and never go beyond 30 words with your answer."),
    ('human', "Question:{question}")
])

def cat(x):
    return ("*"*10+x+"#"*10)

def dfg(x):
    return("This is the output of gpt 3.5 turbo \n\n"+x)
o1 = RunnableLambda(lambda x:cat(x))
o2= RunnableLambda(lambda x:dfg(x))
st.title("demochat")
input_text=st.text_input("Ask based on your Need")
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser|o1|o2
if input_text:
    st.write(chain.invoke({'question':input_text}))
