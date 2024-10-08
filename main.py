import tkinter as tk
import openai
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave de API de OpenAI desde las variables de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Máquina Adivinadora")

# Resto del código de la aplicación...

root.mainloop()
