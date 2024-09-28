import streamlit as st
import json
from src.scraper import scrape_data

# Set the title of the app
st.title("Market Hypothesis Validation")

with st.form("my_form"):
    st.write("Inside the form")

    # Input fields for company information
    company_website = st.text_input("Company Website URL")
    uploaded_files = st.file_uploader("Upload Files", accept_multiple_files=True)
    company_name = st.text_input("Company Name")
    location = st.text_input("Location")
    company_description = st.text_area("Company Description")
    product_description = st.text_area("Detailed Product/Service Description")
    main_message = st.text_area("Main Message")
    target_customer = st.text_area("Target Customer")
# Add checkboxes for B2B, B2C, or B2B2C
    st.write("Are your customers primarily businesses (B2B), individual consumers (B2C), or both (B2B2C)?")
    customer_b2b = st.checkbox("B2B")
    customer_b2c = st.checkbox("B2C")
    customer_b2b2c = st.checkbox("B2B2C")

    # Add checkboxes for market type
    st.write("How do your customers typically use your product?")
    market_physical = st.checkbox("Physical Product")
    market_digital = st.checkbox("Digital Product")
    market_service = st.checkbox("Service")

    # Color picker for selecting a color
    selected_color = st.color_picker("Pick a Color")

    # Add a file uploader
    logo_upload = st.file_uploader("Upload Logo", accept_multiple_files=True)

    # Submit button
    submitted = st.form_submit_button("Submit")

    if submitted:

        company_website_data = scrape_data(company_website)
        st.write(company_website_data)
        company_data = {'company_website': company_website, 'company_name': company_name, 'location': location,
                        'company_description': company_description, 'product_description': product_description,
                        'main_message': main_message, 'target_customer': target_customer, 'customer_b2b': customer_b2b,
                        'customer_b2c': customer_b2c, 'customer_b2b2c': customer_b2b2c, 'market_physical': market_physical,
                        'market_digital': market_digital, 'market_service': market_service, 'logo_upload': logo_upload, 
                        'company_website_data': company_website_data}

        with open("company_data.json", "w") as f:
            json.dump(company_data, f)