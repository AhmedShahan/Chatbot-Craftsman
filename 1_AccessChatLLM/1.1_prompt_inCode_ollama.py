from langchain_ollama import ChatOllama

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
prompt="What is the capital of Bangladesh"

responseDeepSeek=modeldeepseek.invoke(prompt)
responsellama=modelLLama.invoke(prompt)
responseGemma=modelGemma.invoke(prompt)

print("Deepseek Response")
print(responseDeepSeek.content)
print("*"*100)
print("LLama Response")
print(responsellama.content)
print("*"*100)

print("Gemma Response")
print(responseGemma.content)
print("*"*100)
