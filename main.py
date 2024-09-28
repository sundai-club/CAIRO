import json
import streamlit as st
from src.hypothesis_generator import generate_hypothesis
from src.openai_api import OpenAIApi
from src.prompts import hypotheis_update_prompt
from src.utils import parse_llm_response


openai_api = OpenAIApi()

st.set_page_config(layout="wide")

st.header("Welcome to CAIRO: Chief AI Revenue Officer")


st.markdown(
            (
                '<hr style="background-color: #71eea8; margin-top: 0;'
                ' margin-bottom: 0; height: 3px; border: none; border-radius: 3px;">'
            ),
            unsafe_allow_html=True,
        )



with st.form("Get Company Information"):
    st.write("Please Input Company Information below")

    col1, col2 = st.columns([3,4])

    # Input fields for company information
    with col1:
        company_name = st.text_input("Company Name",placeholder="Company Name")
        company_website = st.text_input("Company Website URL")
        # Color picker for selecting a color
        selected_color = st.color_picker("Pick a Brand Color")
        logo_upload = st.file_uploader("Upload Logo", accept_multiple_files=True)
        location = st.text_input("Location")
        # Add checkboxes for market type
        st.write("How type of product are you trying to sell?")
        market_physical = st.checkbox("Physical Product")
        market_digital = st.checkbox("Digital Product")
        market_service = st.checkbox("Service")
        main_message = st.text_area("Main Message")
    with col2:
        company_description = st.text_area("Company Description")
        product_description = st.text_area("Detailed Product/Service Description")
        st.write("What is your Business Model")
        customer_b2b = st.checkbox("B2B")
        customer_b2c = st.checkbox("B2C")
        customer_b2b2c = st.checkbox("B2B2C")
        target_customer = st.text_area("Target Customer")

    # TODO: Add a chat bot

    # Submit button
    submitted = st.form_submit_button("Submit")

    if submitted:
        # Output the form inputs
        st.write("Company Website:", company_website)
        st.write("Company Name:", company_name)
        st.write("Location:", location)
        st.write("Company Description:", company_description)
        st.write("Product/Service Description:", product_description)
        st.write("Main Message:", main_message)
        st.write("Target Customer:", target_customer)
        st.write("Customer Type - B2B:", customer_b2b)
        st.write("Customer Type - B2C:", customer_b2c)
        st.write("Customer Type - B2B2C:", customer_b2b2c)
        st.write("Market Type - Physical Product:", market_physical)
        st.write("Market Type - Digital Product:", market_digital)
        st.write("Market Type - Service:", market_service)
        st.write("Selected Color:", selected_color)

        form_data = {
            "company_website": company_website,
            "company_name": company_name,
            "location": location,
            "company_description": company_description,
            "product_description": product_description,
            "main_message": main_message,
            "target_customer": target_customer,
            "customer_b2b": customer_b2b,
            "customer_b2c": customer_b2c,
            "customer_b2b2c": customer_b2b2c,
            "market_physical": market_physical,
            "market_digital": market_digital,
            "market_service": market_service,
            "selected_color": selected_color,
            "logo_upload": [file.name for file in logo_upload] if logo_upload else []
        }

        form_data_json = json.dumps(form_data)

        hypothesis = generate_hypothesis(form_data_json)

        if 'hypothesis' not in st.session_state:
            st.session_state.hypothesis = hypothesis
        
        if 'conversation' not in st.session_state:
            st.session_state.conversation = []

        



        st.write("Hypothesis:", hypothesis)

        # TODO: 2 RANK THE LIST OF LEADS ASYNC

        # TODO: 3 CREATE THE DECKS ASYNC

if 'hypothesis' in st.session_state:
    st.subheader("Confirm the Hypothesis")

    # Display conversation history
    for message in st.session_state.conversation:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if user_input := st.chat_input("Please let me know if you would like to correct any of the hypothesis if you are not satisfied with the result"):
        # Add user message to conversation
        st.session_state.conversation.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Generate LLM response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            input_prompt = hypotheis_update_prompt.format(
                company_details=st.session_state.conversation,
                hypotheses=st.session_state.hypothesis,
                conversation_history=json.dumps(st.session_state.conversation),
                user_input=user_input
            )
            messages = [{"role": "user", "content": input_prompt}]
            full_response = openai_api.get_completion(messages)
            new_hypothesis = parse_llm_response(full_response)
            message_placeholder.markdown(full_response)
        
        # Add assistant response to conversation
        st.session_state.conversation.append({"role": "assistant", "content": full_response})

    # "Done" button to end the conversation
    if st.button("Done"):
        st.write("Chat session ended. Thank you for using CAIRO!")
        # Here you can add any wrap-up logic or final processing