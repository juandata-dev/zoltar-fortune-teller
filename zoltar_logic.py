import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create the model instance
model = genai.GenerativeModel('gemini-pro')

def get_fortune(question: str) -> str:
    """Gets a fortune from the Gemini API."""
    try:
        if not question.strip():
            return "Por favor, haz una pregunta."

        # Prepare the prompt for the fortune teller response
        prompt = f"""Eres Zoltar, una misteriosa máquina de adivinación. 
        Un solicitante pregunta: '{question}'
        Da una respuesta de adivino místico, entretenida en otras ocasiones macabra o funestao o con humor negro en 2-3 frases."""

        # Make API call with proper error handling
        response = model.generate_content(prompt)
        if hasattr(response, 'text') and response.text:
            return response.text.strip()
        else:
            return "Las brumas del destino están oscuras. Inténtalo de nuevo."
    
    except Exception as e:
        if "HARM" in str(e):
            return "Las fuerzas místicas están confusas. Inténta preguntar algo diferente."
        return f"Las fuerzas místicas no están disponibles temporalmente..."
