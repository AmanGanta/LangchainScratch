from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage,AIMessage
load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
Memory = []  
Memory.append(SystemMessage(content="You are a helpful AI assistant."))  
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    Memory.append(HumanMessage(content=query))  

    result = llm.invoke(Memory)
    response = result.content
    Memory.append(AIMessage(content=response))  

    print(f"AI: {response}")

print("*********Memory*********")
print(Memory)
