from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere
from langchain_ollama import ChatOllama
modelGemini= ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.1
)
modelCohera= ChatCohere(model="command-r-plus")
modeldeepseek=ChatOllama(
    model="deepseek-r1:latest",
    temprature=0.9
)

modelLLama=ChatOllama(
    model="llama3.2:latest",
    temprature=0.9
)

modelGemma=ChatOllama(
    model="gemma3:latest",
    temprature=0.9
)

while True:
    prompt = input("Enter your prompt: ")
    if prompt.lower() == "exit":
        break
    response_gemini= modelGemini.invoke(prompt)
    response_cohera = modelCohera.invoke(prompt)
    response_deepseek=modeldeepseek.invoke(prompt)
    response_llmama=modelLLama.invoke(prompt)
    response_gemma=modelGemma.invoke(prompt)

    print("Cohere Response:",end=":")
    print(response_cohera.content)
    print("*"*50)
    
    print("Gemini Response:",end=":")
    print(response_gemini.content)
    print("*"*50)
    
    print("DeepSeek Response:",end=":")
    print(response_deepseek.content)
    print("*"*50)
    
    print("LLama Response:",end=":")
    print(response_llmama.content)
    print("*"*50)

    print("Gemma Response:",end=":")
    print(response_gemma.content)
    print("*"*50)