from langchain_google_genai import ChatGoogleGenerativeAI

model= ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.1
)

response= model.invoke(
    "What is the capital of France?"
)
print(response.content)