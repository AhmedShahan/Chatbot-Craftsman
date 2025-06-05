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
    ChatHistory.append(response_gemini.content)
    
    print("\nGemini Response:",end=":")
    print(response_gemini.content)
    print("*"*50)

print(ChatHistory)

'''
PROBLEM IN THIS CHAT HISTORY

['what is the largest of 10,22,21,11', 
'The largest number among 10, 22, 21, and 11 is $\\boxed{22}$.', 
'multiply with 10 with largest number', 
'The largest number is 22.  22 multiplied by 10 is 220.', 
'now substract the result from lowest number', 
'The lowest number is 10.  Subtracting 220 from 10 gives 10 - 220 = -210', 
'exit']


এখানে কোন চেট কীসের সেটা বুঝা জায় না। মানে কোনটা user এর prompt আর কোনটা AI এর response সেটা বুঝা জায় না। 
'''