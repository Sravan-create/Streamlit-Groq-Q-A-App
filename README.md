Streamlit Groq Q&A App
A simple Streamlit application that allows users to ask questions to a Groq LLM based on context extracted from Wikipedia using a FAISS vector store.

<br>
🚀 Features
Load context from a webpage (Wikipedia) using WebBaseLoader

Split text into chunks with RecursiveCharacterTextSplitter

Generate embeddings using OllamaEmbeddings

Store and retrieve chunks using FAISS

Answer questions with Groq LLM (llama-3.1-8b-instant)

Interactive front-end using Streamlit

<br>
📂 Project Structure
end-to-end project/
└── app.py    # Main Streamlit application
<br>
🔧 Setup Instructions
Clone the repository

git clone https://github.com/Sravan-create/Streamlit-Groq-Q-A-App.git
cd Streamlit-Groq-Q-A-App
Install dependencies

pip install -r requirements.txt
Run the Streamlit app

streamlit run "end-to-end project/app.py"
Open in your browser:
http://localhost:8501

<br>
📋 Example Usage
Input:

"What types of chocolate are there?"

Output:

Intelligent answer fetched from Wikipedia + Groq LLM.

✅ Next Steps
Create a README.md file with the above text.

Push it:

git add README.md
git commit -m "Added minimal clean README.md"
git push
