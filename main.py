import streamlit as st

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
        uploaded_files = st.file_uploader("Upload Logo", accept_multiple_files=True)
        location = st.text_input("Location")
        # Add checkboxes for market type
        st.write("How type of product are you trying to sell?")
        market_physical = st.checkbox("Physical Product")
        market_digital = st.checkbox("Digital Product")
        market_service = st.checkbox("Service")
    with col2:
        company_description = st.text_area("Company Description")
        product_description = st.text_area("Detailed Product/Service Description")
        st.write("What is your Business Model")
        customer_b2b = st.checkbox("B2B")
        customer_b2c = st.checkbox("B2C")
        customer_b2b2c = st.checkbox("B2B2C")

    main_message = st.text_area("Main Message")
    target_customer = st.text_area("Target Customer")
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