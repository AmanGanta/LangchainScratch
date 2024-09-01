from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
llm=ChatOpenAI(model="gpt-3.5-turbo")
res=llm.invoke("Sum of 2 numbers is even then what will their product even or odd?")
print("\n")
print("FULL ANSWER IS: \n")
print(res)
print("\n\n")
print(res.content)