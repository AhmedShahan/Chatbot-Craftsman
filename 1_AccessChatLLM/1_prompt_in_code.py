from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere

modelGemini= ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.1
)

modelCohera= ChatCohere(model="command-r-plus")

prompt = "What is AI? Explain in simple terms and 5 lines"

response_gemini= modelGemini.invoke(prompt)
response_cohera = modelCohera.invoke(prompt)
print("Cohere Response:")
print(response_cohera.content)
print("Gemini Response:")
print(response_gemini.content)