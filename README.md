# 💬 AI-Powered Health Assistant

This is a Streamlit-based AI chatbot designed to provide general health guidance using rule-based responses and a fallback AI model from Hugging Face Transformers.

---

## 🚀 Features

- 🧠 Intelligent responses to health-related queries
- 🔍 Rule-based logic for common topics (symptoms, appointments, medications, etc.)
- 🤖 Fallback to a text-generation AI model (`distilgpt2`) for general queries
- 💡 Tips on nutrition, mental health, exercise, and more
- 🔄 Session memory with Streamlit to handle chat interactions

---

## 🛠️ Installation

  1.  	**conda activate ./health**  
	**pip install -r .\requirements.txt** 
	**streamlit run healthcare_chatbot.py**


**NOTE** :

On **Windows**, there's **no need to install `tkinter`**, as it comes pre-installed with Python. Additionally, **base64**, **hashlib**, and many other utility libraries used are part of Python's standard library.

---

# All information about Files and Folders:-

### 1) Main App File:
The main file is named **"healthcare_chatbot.py"**. This is a **Streamlit web application** that serves as a simple AI health assistant. It uses **rule-based responses** and a **Hugging Face Transformers model (`distilgpt2`)** to provide answers to health-related queries.

When you run this file using Streamlit, it launches a local web interface where users can interact with the assistant.

---

### 2) requirements.txt:
This file lists all the Python packages needed to run the chatbot. To install everything in one go, run:

pip install -r requirements.txt


# Project Image:-

![Image](https://github.com/user-attachments/assets/b03c5cb1-de76-4fa5-87f4-d37a52ac0f16)

# Project Video:-

https://github.com/user-attachments/assets/d29f0380-7772-46c4-87ef-0a545512b034
