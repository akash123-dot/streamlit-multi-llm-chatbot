## Q&A Chatbot using Streamlit

This is a simple and clean **Q&A Chatbot application** built using **Streamlit** and powered by three LLM providers:

- **Google Gemini 2.5 Flash**
- **HuggingFace (DeepSeek-R1 endpoint)**
- **Groq (OpenAI GPT-OSS-120B)**

The user can:
- Select which model they want to use
- Adjust the **temperature** value
- Ask any question and get an instant response

## 🚀 Features
- Streamlit UI
- Dynamic model selection
- Adjustable temperature slider
- Uses LangChain for prompt + LLM chaining
- Simple and beginner‑friendly architecture

## 🛠️ Tech Stack
- **Python**
- **Streamlit**
- **LangChain**
- **Gemini API**
- **HuggingFace Inference API**
- **Groq API**


## 🔑 Environment Variables
Create a `.env` file with the following variables:
```
GOOGLE_API_KEY=your_google_key
HUGGINGFACEHUB_API_TOKEN=your_hf_token
GROQ_API_KEY=your_groq_key

```

## ▶️ How to Run
1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run the app:
```
streamlit run app.py
```

## 📝 Notes
- `.env` and `.venv` are excluded from the repository for security.
- LangSmith is optional but supported when API keys are provided.

## 📜 License
This project is for educational and personal use. Feel free to modify and enhance it.

