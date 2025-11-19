import streamlit as st

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("user", "Question:{question}"),
    ]
)

def generate_response(question,temparature):
    try:
        if model_choice == "google-Gemini-2.5-flash":
            llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=temparature,
            max_tokens= None,
            timeout=None,
            max_retries=6,
            api_key=os.getenv('GOOGLE_API_KEY'),
            )

        elif model_choice == "HuggingFace":
            HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')
            llm = HuggingFaceEndpoint(
            repo_id="deepseek-ai/DeepSeek-R1-0528",
            task="text-generation",
            max_new_tokens=512,
            do_sample=False,
            repetition_penalty=1.03,
            provider="auto" 
            )
            llm = ChatHuggingFace(llm=llm)


        elif model_choice == "Groq-4":
            llm = ChatGroq(
            model="openai/gpt-oss-120b",
            temperature=temparature,
            max_tokens=None,
            reasoning_format="parsed",
            timeout=None,
            max_retries=2,
            api_key=os.getenv('GROQ_API_KEY'),
            )
        
        chain = prompt|llm|StrOutputParser()
        answer = chain.invoke({"question": question})
        return answer
    except Exception as e:
        return str(e)



st.title("Enhanced Q&A Chatbot")

st.sidebar.title("Settings")

model_choice=st.sidebar.selectbox("Select an Open AI Model",["google-Gemini-2.5-flash", "HuggingFace", "Groq-4"])

temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)

st.write("Go ahead and ask any question")
user_input=st.text_input("You:")

## Generate response
if user_input:
    response = generate_response(user_input, temperature)
    st.write("Bot:",response)
else:
    st.write("Please enter a question")
