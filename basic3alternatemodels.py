from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage,AIMessage
load_dotenv()

msg=[SystemMessage(content="Solve the follwoing Math trick questions"),
     HumanMessage(content="Sum of 2 numbers is even then what will their product even or odd?"),
     AIMessage(content="f the sum of two numbers is even, then their product can be either even or odd.For example, consider the numbers 2 and 4. Their sum is 6 (even) and their product is 8 (even).But, if we consider the numbers 3 and 4, their sum is 7 (odd) and their product is 12 (even).So, the product of two numbers whose sum is even can be either even or odd."),
HumanMessage("Then could be the result of division and subtration answer me in one line")
     ]
model = ChatAnthropic(model="claude-3-opus-20240229")

result = model.invoke(msg)
print(f"Answer from Anthropic: {result.content}")

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

result = model.invoke(msg)
print(f"Answer from Google: {result.content}")