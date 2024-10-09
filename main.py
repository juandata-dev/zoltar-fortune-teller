import tkinter as tk
from PIL import Image, ImageTk
import google.generativeai as genai
import os
from tkinter import messagebox
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create the model instance
model = genai.GenerativeModel('gemini-pro')

# Function to get fortune from Gemini API
def get_fortune():
    try:
        user_question = entry.get()
        if not user_question.strip():
            messagebox.showwarning("Warning", "Please enter a question!")
            return

        # Update UI to show loading state
        result_label.config(text="🔮 Consulting the mystic forces... 🔮")
        root.update()

        # Prepare the prompt for the fortune teller response
        prompt = f"""You are Zoltar, a mysterious fortune teller machine. 
        A seeker asks: '{user_question}'
        Give a mystical and entertaining fortune teller response in 2-3 sentences."""

        # Make API call with proper error handling
        response = model.generate_content(prompt)
        
        fortune = response.text.strip()
        result_label.config(text=fortune)
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        result_label.config(text="The mystic forces are temporarily unavailable...")

# Setting up the GUI
root = tk.Tk()
root.title("Zoltar Fortune Teller")
root.geometry("1920x1080")

try:
    # Load and display the Zoltar image as the background
    zoltar_image = Image.open("./assets/zoltar.jpg")
    zoltar_image = zoltar_image.resize((1920, 1080), Image.Resampling.LANCZOS)
    zoltar_photo = ImageTk.PhotoImage(zoltar_image)

    # Create a Canvas to hold the background image
    canvas = tk.Canvas(root, width=1920, height=1080)
    canvas.pack(fill="both", expand=True)

    # Add the image to the canvas as the background
    canvas.create_image(0, 0, image=zoltar_photo, anchor="nw")

    # Create styled widgets
    title_label = tk.Label(
        root, 
        text="🔮 Ask Zoltar Your Question 🔮",
        font=("Arial", 16, "bold"),
        bg="white",
        relief="raised",
        padx=10,
        pady=5
    )

    entry = tk.Entry(
        root,
        width=40,
        font=("Arial", 12)
    )

    fortune_button = tk.Button(
        root,
        text="Ask Zoltar",
        command=get_fortune,
        font=("Arial", 12, "bold"),
        bg="#4a90e2",
        fg="white",
        padx=20,
        pady=10
    )

    result_label = tk.Label(
        root,
        text="",
        wraplength=300,
        font=("Arial", 12),
        bg="white",
        relief="sunken",
        padx=10,
        pady=10
    )

    # Place widgets on the canvas with better spacing
    canvas.create_window(200, 50, window=title_label)
    canvas.create_window(200, 150, window=entry)
    canvas.create_window(200, 200, window=fortune_button)
    canvas.create_window(200, 350, window=result_label)

except FileNotFoundError:
    messagebox.showerror("Error", "Could not find the background image file!")
    # Create a basic layout without the background image
    title_label = tk.Label(root, text="Zoltar Fortune Teller", font=("Arial", 16))
    title_label.pack(pady=20)
    entry.pack(pady=20)
    fortune_button.pack(pady=20)
    result_label.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()