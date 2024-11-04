import streamlit as st  # Importing Streamlit for web app development
import google.generativeai as genai  # Importing Google Generative AI library
import os  # Importing OS library to interact with the operating system
from dotenv import load_dotenv  # Importing to load environment variables from .env file
load_dotenv()  # Load environment variables from the .env file
from PIL import Image  # Importing PIL (Python Imaging Library) to handle image processing

# Configure the Generative AI model with the API key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, image):
    """Generates a response using the Gemini AI model based on the input prompt and image provided."""
    model = genai.GenerativeModel('gemini-1.5-pro')  # Instantiate the GenerativeModel with the specific model
    response = model.generate_content([input_prompt, image[0]])  # Generate content based on the input prompt and image
    return response.text  # Return the generated response text

def input_image_setup(uploaded_file):
    """Prepares the uploaded image for processing."""
    if uploaded_file is not None:  # Check if an uploaded file exists
        bytes_data = uploaded_file.getvalue()  # Get the byte data of the uploaded file

        # Create a list containing the MIME type and byte data of the uploaded image
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts  # Return the prepared image parts
    else:
        raise FileNotFoundError("No file uploaded")  # Raise an error if no file is uploaded
    
# Initialize the Streamlit app with a specific page title
st.set_page_config(page_title="Gemini Health App")

st.header("Gemini Health App")  # Display the header for the app
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])  # File uploader for images
image = ""  # Initialize the image variable
if uploaded_file is not None:  # Check if a file has been uploaded
    image = Image.open(uploaded_file)  # Open the uploaded image
    st.image(image, caption="Uploaded Image.", use_column_width=True)  # Display the uploaded image with a caption

submit = st.button("Tell me the total calories")  # Create a submit button

# Define the input prompt for the AI model
input_prompt = """
You are an expert in nutritionist where you need to see the food items from the image
and calculate the total calories, also provide the details of every food items with calories intake
is below format

1. Item 1 - no of calories
2. Item 2 - no of calories
----
----

Finally you can also mention whether the food is healthy or not and also mention
the percentage split of the ratio of carbohydrates, fats, fibers, sugar and other
important things required in our diet
"""

# If the submit button is clicked
if submit:
    image_data = input_image_setup(uploaded_file)  # Prepare the image for processing
    response = get_gemini_response(input_prompt, image_data)  # Get the AI response based on the input prompt and image
    st.subheader("The Response is")  # Display a subheader for the response section
    st.write(response)  # Write the AI's response to the Streamlit app
