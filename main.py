import streamlit as st

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

# Outside the form
st.write("Outside the form - TBD")