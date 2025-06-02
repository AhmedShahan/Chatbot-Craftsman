import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

st.title("🤖 My First Chatbot")

user_input = st.chat_input("Enter Your Query")

modelGemini = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.1
)

if user_input:
    # Display user message with icon
    st.write(f"👤 **You:** {user_input}")
    
    # Show loading spinner while processing
    with st.spinner("🔄 Processing..."):
        response = modelGemini.invoke(user_input)
    
    # Display AI response with icon
    st.write(f"🤖 **AI:** {response.content}")