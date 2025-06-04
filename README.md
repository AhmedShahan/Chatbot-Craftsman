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
<div align="center">
  <h1>🧭 Getting Started</h1>
</div>

## Accessing LLM
 
<details><summary>▶️ 1. PROMPT IN CODE</summary>

This is a basic code basis initial chatbot, Just change the Prompt text and run the code. The print or output will be the response. 
<img src="https://github.com/user-attachments/assets/e5bca00f-6ab1-4c61-b183-6b0f95c39bf6" alt="chatbot1" width="800" height="300">
Main code: https://github.com/AhmedShahan/Chatbot-Craftsman/blob/main/1_AccessChatLLM/1_prompt_in_code.py  

**If you are using GPU then you can use Huggingface or Ollama to access more LLMs**
Install Ollama from the terminal  
```
pip install langchain-ollama
```
Now Install ollama in your PC  
  - For Linux: ```curl -fsSL https://ollama.com/install.sh | sh```
  - For Windows: https://ollama.com/download/windows 
  - For MacOS : https://ollama.com/download/mac   

Now Install LLMs from https://ollama.com/search what you desire and based on your GPU  
  * ```ollama run deepseek-r1```
  * ```ollama run llama3.2```
  * ```ollama run gemma3```


<img src="https://github.com/user-attachments/assets/711092fd-f764-4a94-9bd1-7c9e77583f64" alt="chatbot1" width="800" height="300">  

Main code: https://github.com/AhmedShahan/Chatbot-Craftsman/blob/main/1_AccessChatLLM/1.1_prompt_inCode_ollama.py 
</details>


<details><summary>🖱️⌨️ 2. PROMPT IN TERMINAL</summary>
There will be a while loop where you can prompt and answer. If the user type exit then the chatbot will be terminated.   
        
![chatbot2](https://github.com/user-attachments/assets/799969b5-f6aa-4d68-a7c1-183652b1d370)  

Main code: https://github.com/AhmedShahan/Chatbot-Craftsman/blob/main/1_AccessChatLLM/2_prompt_in_terminal.py  
</details>

<details><summary>🖥️ 3. CHATBOT IN STREAMLIT</summary>
Previous Chatbot in Streamlit UI  
<img src="https://github.com/user-attachments/assets/4ab3a6dd-1be5-4e20-928c-c6c3816407df" alt="chatbot2" width="600" height="800">  


Main Code: https://github.com/AhmedShahan/Chatbot-Craftsman/blob/main/1_AccessChatLLM/3_chatbot_in_streamlit.py  
</details>


<details><summary>⚠️ 4. PROBLEM IN PREVIOUS CHATBOT</summary>
<img src="https://github.com/user-attachments/assets/4ab3a6dd-1be5-4e20-928c-c6c3816407df" alt="chatbot2" width="600" height="800">  

**Explanation**
এখানে প্রথমে বলা হয়েছিল যে সর্বোচ্চ সংখ্যা বের করতে। এটা আমাদের চেটবট পেরেছে।   
কিন্তু প্রব্লেম টা হয়ে গেলো যে পরবর্তিতে যখন বলা হলও যে সবচেয়ে বড় সংখ্যার সাথে ২ দিয়ে গুন দেও, তখন এটা আর লিস্ট পাচ্ছে না বা বড় সংখ্যা পাচ্ছে না।  

কেন এমন হচ্ছে?  
একটু ভেবে দেখি। আমরা prompt দেই সেটা invoke হয়ে Response আসে। তাহলে দ্দদুইবার Prompt andd Response সম্পুর্ন আলাদা আলাদা অস্তিত্ব বহন করে। তার মানে চেটবট আগের কোন কিছুই মনে রাখতে পারছে না।  

সমাধান কী? 
আমরা সবকিছুই তাকে দ্বিয়ে দিবো।  
মানে হলও আমরা চেটবট কে শুধু প্রশ্নও করবও না সাথে করে History ও দিয়ে দিব। 

Main Code: https://github.com/AhmedShahan/Chatbot-Craftsman/blob/main/1_AccessChatLLM/5_problemInPreviousChatbot.py  
</details>


<details><summary>🧨 5. SOLUTION OF THE CHATBOT. METHOD:1</summary>


We can use a list. Every time we will append the list and while invoke **WE WILL PASS THE ENTIRE LIST**
<img src="https://github.com/user-attachments/assets/4ab3a6dd-1be5-4e20-928c-c6c3816407df" alt="chatbot2" width="600" height="800">  



Main Code: https://github.com/AhmedShahan/Chatbot-Craftsman/blob/main/1_AccessChatLLM/3_chatbot_in_streamlit.py  
</details>
