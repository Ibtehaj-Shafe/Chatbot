import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
# -------------------Dashboard--------------------

st.set_page_config(layout="wide")
st.title("Chatbot!")
st.subheader("Groq Open ai")

st.markdown("---")

user_question =  st.text_input("Enter query : ")
ask_button = st.button(label="Ask")

#-----------------loading Groq API--------------------------
load_dotenv()
groq_api_key = os.getenv("groq_api_key")

#-----------------Implement Groq--------------------------
client = Groq(api_key=groq_api_key)


if ask_button:
    if user_question:
        st.write("Processing request")
        response = client.chat.completions.create(
            model = "llama-3.1-8b-instant",
             messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_question}
            ],
        )
        answer = response.choices[0].message.content
        st.subheader("Response:")
        st.write(answer)

