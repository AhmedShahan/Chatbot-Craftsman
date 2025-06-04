from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere
from langchain_ollama import ChatOllama
modelGemini= ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.1
)

while True:
    prompt = input("Enter your prompt: ")
    if prompt.lower() == "exit":
        break
    response_gemini= modelGemini.invoke(prompt)
    
    print("\nGemini Response:",end=":")
    print(response_gemini.content)
    print("*"*50)