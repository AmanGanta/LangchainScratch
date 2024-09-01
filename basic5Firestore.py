from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_firestore import FirestoreChatMessageHistory
from google.cloud import firestore
load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
PROJECT_ID="deepamanlangchain"
SESSION_ID = "session_1"  
COLLECTION_NAME = "Memory"

client = firestore.Client(project=PROJECT_ID)

print("Initializing Firestore Chat Message History...")
Memory = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)
print("Chat History Initialized.")
print("Current Chat History:", Memory.messages)

while True:
    human_input = input("User: ")
    if human_input.lower() == "exit":
        break
    Memory.add_user_message(human_input)

    ai_response = llm.invoke(Memory.messages)
    Memory.add_ai_message(ai_response.content)

    print(f"AI: {ai_response.content}")