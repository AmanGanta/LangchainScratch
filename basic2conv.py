from langchain_community.chat_models import ChatOpenAI
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
from dotenv import load_dotenv
load_dotenv()
llm=ChatOpenAI(model="gpt-3.5-turbo")

msg=[SystemMessage(content="Solve the follwoing Math trick questions"),
     HumanMessage(content="Sum of 2 numbers is even then what will their product even or odd?")
     ]
res=llm.invoke(msg)
print("\n")
print("FULL ANSWER IS: \n")
print(res)
print("\n\n")
print(res.content)

msg=[SystemMessage(content="Solve the follwoing Math trick questions"),
     HumanMessage(content="Sum of 2 numbers is even then what will their product even or odd?"),
     AIMessage(content="f the sum of two numbers is even, then their product can be either even or odd.For example, consider the numbers 2 and 4. Their sum is 6 (even) and their product is 8 (even).But, if we consider the numbers 3 and 4, their sum is 7 (odd) and their product is 12 (even).So, the product of two numbers whose sum is even can be either even or odd."),
HumanMessage("Then could be the result of division and subtration answer me in one line")
     ]


res=llm.invoke(msg)
print("\n")
print("FULL ANSWER IS: \n")
print(res)
print("\n\n")
print(res.content)