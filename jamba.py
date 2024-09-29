import streamlit as st
from src.openai_api import OpenAIApi, JambaAIApi
from src.utils import parse_llm_response
import os 
import html
import csv


envs={}
for row in csv.reader(open(".env"),delimiter='='):
        envs[row[0]]=row[1]

api_key=envs["JAMBA_KEY"]
client = JambaAIApi(api_key=api_key)

st.title("Jamba Chat")

# Initialize session state to store the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if user_input := st.chat_input("Type your message"):
    # Add the user's message to the chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display the user's message
    with st.chat_message("user"):
        st.markdown(user_input)


    messages = [{"role": "user", "content": "translate user's message to spanish. Limit the response to 30 words maximum. Message:"+user_input}]

    answer = client.get_completion(messages)
    # Add the assistant's response to the chat history
    st.session_state.messages.append({"role": "assistant", "content": answer})

    # Display the assistant's response
    with st.chat_message("assistant"):
        st.markdown(html.unescape(answer))
