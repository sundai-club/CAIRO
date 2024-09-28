import streamlit as st

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

    # **Custom Logic Placeholder**
    # Here you can add your custom logic to process the user_input
    # For example, you can integrate an AI model, perform calculations, etc.
    # Replace the response below with your logic
    response = f"You said: {user_input}"

    # Add the assistant's response to the chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Display the assistant's response
    with st.chat_message("assistant"):
        st.markdown(response)
