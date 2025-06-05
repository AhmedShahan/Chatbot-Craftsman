from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere
from langchain_ollama import ChatOllama

from dotenv import load_dotenv
load_dotenv()
modelGemini= ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.1
)
ChatHistory=[]
while True:
    prompt = input("Enter your prompt: ")
    ChatHistory.append(prompt)
    if prompt.lower() == "exit":
        break
    response_gemini= modelGemini.invoke(ChatHistory)
    ChatHistory.append(response_gemini)
    
    print("\nGemini Response:",end=":")
    print(response_gemini.content)
    print("*"*50)