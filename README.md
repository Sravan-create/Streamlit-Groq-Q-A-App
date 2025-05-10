# Streamlit Groq Q&A App

A simple **Streamlit** application that allows users to **ask questions** to a **Groq LLM** based on **context extracted from Wikipedia** using a **FAISS** vector store.

## 🚀 Features
- Load context from a webpage (Wikipedia) using `WebBaseLoader`
- Split text into chunks with `RecursiveCharacterTextSplitter`
- Generate embeddings using `OllamaEmbeddings`
- Store and retrieve chunks using `FAISS`
- Answer questions with **Groq LLM** (`llama-3.1-8b-instant`)
- Interactive front-end using **Streamlit**

## 📂 Project Structure
end-to-end project/
└── app.py # Main Streamlit application

bash
Copy
Edit

## 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sravan-create/Streamlit-Groq-Q-A-App.git
   cd Streamlit-Groq-Q-A-App
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app

bash
Copy
Edit
streamlit run "end-to-end project/app.py"
Open in your browser:

arduino
Copy
Edit
http://localhost:8501
📋 Example Usage
Input:

"What types of chocolate are there?"

Output:

Intelligent answer fetched from Wikipedia + Groq LLM.

yaml
Copy
Edit
