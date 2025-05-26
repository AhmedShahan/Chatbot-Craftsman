# 🚀 Chatbot-Craftsman: All Your Chatbots, Built from Scratch! 🤖

Welcome to **Chatbot-Craftsman**, the ultimate repository where you can create powerful AI chatbots from the ground up! This project provides clear, step-by-step instructions to set up and integrate with leading AI APIs. Let’s get started building your chatbot masterpiece! ✨

---

## 🎯 What is Chatbot-Craftsman?  
Chatbot-Craftsman is an open-source repository designed to empower developers to build chatbots using popular AI APIs like OpenAI, Google Gemini, Cohere, and Hugging Face. This repo includes step-by-step instructions, sample code, and best practices to help you create intelligent, conversational agents with ease.

* Why use it?  
        - Build chatbots from scratch with minimal setup.  
        - Integrate with multiple AI platforms.
Perfect for learning, experimenting, or deploying production-ready bots.

## 🛠️ Getting Started
Follow these simple steps to set up your development environment and start crafting your chatbot masterpiece! 🎨

### 1. Clone the Repository
Get the code onto your local machine:
```
git clone github.com/AhmedShahan/Chatbot-Craftsman.git 
```

### 2. Go inside the Repository
* Either UI based (Double Click on the folder ```Chatbot-Craftsman```)  
* or Using Command ```Chatbot-Craftsman```

### 3.🐍 Setting up your Virtual Environment
Set up an isolated Python environment to keep your dependencies organized:
* For Windows, Linux or MacOS  
```python -m venv myvenv```  
or   
```python3 -m venv myvenv```

### 3. ✅ Activate the Virtual Environment
- For windows: ```myvenv/Scripts/activate``` 
- For Linux : ```source myvenv/bin/activate```

### 4. 🔐 Add Your API Keys
Create a ```.env``` file in the project root and add your API keys like this:
```
OPENAI_API_KEY="your-openai-api"
GOOGLE_API_KEY="your-gemini-api"
COHERE_API_KEY="your-cohere-api"
HUGGINGFACEHUB_API_TOKEN="your-huggingface-api"
```
### 📦 Install Dependencies
Install all required packages:  
```
pip install -r requirements.txt
```
<details>
  <summary><strong>🧠 Accessing LLM</strong></summary>

  <ul>
    <li>🧾 <strong>Prompt in Code</strong> – Directly use Python scripts to interact with LLMs using API calls.</li>
    <li>💻 <strong>Prompt in Terminal (Unlimited Chat)</strong> – Chat with your model directly via command line in an unlimited loop.</li>
    <li>🌐 <strong>Prompt in Streamlit</strong> – Launch a lightweight Streamlit app for a clean UI experience.</li>
    <li>🗂 <strong>Chat History</strong> – Store and retrieve previous interactions from local memory or database.</li>
    <li>📜 <strong>Streamlit Access with History</strong> – Use the web interface with session-based or saved conversation history.</li>
  </ul>

</details>