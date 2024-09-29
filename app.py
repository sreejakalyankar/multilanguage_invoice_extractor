from dotenv import load_dotenv
load_dotenv()  # Loads all the environment variables from .env

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Configure the API key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load the Gemini AI Model
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_invoice_response(user_input, invoice_image, ai_prompt):
    response = model.generate_content([user_input, invoice_image[0], ai_prompt])
    return response.text

def extract_image_details(uploaded_image):
    if uploaded_image is not None:
        # Convert the uploaded image to byte data
        image_byte_data = uploaded_image.getvalue()

        image_metadata = [
            {
                'mime_type': uploaded_image.type,  # MIME type of the uploaded image
                'data': image_byte_data
            }
        ]
        return image_metadata
    else:
        raise FileNotFoundError('No image uploaded')

# Initialize the Streamlit app
st.set_page_config(page_title='Multi-Language Invoice Extractor')
st.header('Multi-Language Invoice Extractor')

user_query = st.text_input('Enter a query regarding the invoice:', key='user_query')

uploaded_image = st.file_uploader('Upload an invoice image', type=['jpg', 'jpeg', 'png'])
image_display = ''

if uploaded_image is not None:
    image_display = Image.open(uploaded_image)
    st.image(image_display, caption='Uploaded Invoice Image', use_column_width=True)

submit_button = st.button('Analyze Invoice')

invoice_analysis_prompt = '''
You are an expert in understanding invoices. An image of an invoice will be uploaded, 
and you will be required to answer any questions related to the content of the invoice.
'''

if submit_button:
    image_metadata = extract_image_details(uploaded_image)
    ai_response = generate_invoice_response(invoice_analysis_prompt, image_metadata, user_query)
    st.subheader('Invoice Analysis Result:')
    st.write(ai_response)
