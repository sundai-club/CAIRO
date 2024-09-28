import streamlit as st
from ai21 import AI21Client
from ai21.models.chat import UserMessage
import os 
import html
import csv

envs={}
for row in csv.reader(open(".env"),delimiter='='):
        envs[row[0]]=row[1]

api_key=envs["JAMBA_KEY"]
client = AI21Client(api_key=api_key)

st.title("Chat Interface with Custom Logic")

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

    messages = [
        UserMessage(
            content="translate user's message to spanish. Limit the response to 30 words maximum. Message:"+user_input
        )
    ]

    response = client.chat.completions.create(
        model="jamba-1.5-large",
        messages=messages,
        top_p=1.0 # Setting to 1 encourages different responses each call.
    )
    response = str(response.choices[0].message.content)

    # Add the assistant's response to the chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Display the assistant's response
    with st.chat_message("assistant"):
        st.markdown(html.unescape(response))
