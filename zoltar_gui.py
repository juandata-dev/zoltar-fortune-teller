import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from zoltar_logic import get_fortune

def create_gui():
    """Creates the main GUI window and handles user interaction."""
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

        def display_fortune():
            """Gets the fortune and updates the result label."""
            user_question = entry.get()
            fortune = get_fortune(user_question)
            result_label.config(text=fortune)

        fortune_button = tk.Button(
            root,
            text="Ask Zoltar",
            command=display_fortune,
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

if __name__ == "__main__":
    create_gui()
