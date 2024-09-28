import json
import streamlit as st
from src.hypothesis_generator import generate_hypothesis


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
        st.write("Uploaded Files:", uploaded_files)
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

        # Convert dictionary to JSON string
        form_data_json = json.dumps(form_data)

        # Output the JSON
        # st.write("Form Data as JSON:")
        # st.json(form_data_json)

        hypothesis = generate_hypothesis(form_data_json)

        st.write("Hypothesis:", hypothesis)

        # TODO: 2 RANK THE LIST OF LEADS ASYNC

        # TODO: 3 CREATE THE DECKS ASYNC
