# Health App

## Overview
The Health App is a Streamlit-based web application that helps users analyze food images to calculate total calorie intake. Utilizing the Google Gemini model, the app provides detailed nutritional information about the food items detected in the uploaded images.

## Features
- Upload an image of food items (JPG, JPEG, PNG formats).
- Analyze the image to extract food items and their corresponding calorie counts.
- Generate a nutritional summary, including the total calorie intake and the percentage split of macronutrients.

## Technologies Used
- **Python**: Programming language for backend logic.
- **Streamlit**: Framework for building the web application.
- **Google Generative AI**: For generating responses based on nutritional analysis.
- **PIL (Pillow)**: For image handling.
- **dotenv**: For managing environment variables.

## Installation
Follow these steps to set up the project locally:

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/gemini-health-app.git
   cd gemini-health-app
   ```
2. **Create a virtual environment**
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. **Install the required packages**
```
pip install -r requirements.txt
```
4. **Set up your Google API key**
* Create a .env file in the root directory of the project and add your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```
5. **Run the application**
```
streamlit run app.py
```
## Usage
1. Open your web browser and go to http://localhost:8501.
2. Upload a food image using the file uploader.
3. Click on the "Tell me the total calories" button to analyze the image.
4. View the generated nutritional information on the screen.



      

   
