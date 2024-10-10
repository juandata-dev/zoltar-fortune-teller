import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from zoltar_logic import get_fortune
import pygame  # Import pygame for audio
import random

def create_gui():
    """Creates the main GUI window and handles user interaction."""
    root = tk.Tk()
    root.title("Zoltar Fortune Teller")
    root.geometry("1920x1080")

    # Initialize Pygame mixer for audio playback
    pygame.mixer.init()

    # List of audio files to play randomly
    audio_files = [
        "./assets/227_Terror_in_the_Woods.mp3",
        "./assets/252_Vault_of_Terror.mp3",
        "./assets/308_Skullwharf.mp3",
        "./assets/344_Yokai_Forest.mp3",
        "./assets/352_Black_Rider.mp3",
        "./assets/354_Warlocks_Whisper.mp3",
        "./assets/388_Lord_of_Bones.mp3",
        "./assets/394_Demon_Army.mp3",
        "./assets/404_Vampyr.mp3",
        "./assets/430_Fire_Dance.mp3"
    ]

    def play_random_music():
        """Plays a random audio file from the audio_files list."""
        if not audio_files:
            print("No audio files to play.")
            return

        # Choose a random audio file
        audio_file = random.choice(audio_files)
        print(f"Playing: {audio_file}")
        
        # Load and play the audio file
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play(-1)  # Play the music indefinitely

    try:
        play_random_music()  # Play a random audio file

        # Load and display the Zoltar image as the background
        zoltar_image = Image.open("./assets/background.jpg")
        zoltar_image = zoltar_image.resize((1920, 1080), Image.Resampling.LANCZOS)
        zoltar_photo = ImageTk.PhotoImage(zoltar_image)

        # Create a Canvas to hold the background image
        canvas = tk.Canvas(root, width=1920, height=1080)
        canvas.pack(fill=tk.BOTH, expand=True)

        # Add the image to the canvas as the background
        canvas.create_image(0, 0, image=zoltar_photo, anchor="nw")

        # Create styled widgets
        entry = tk.Entry(
            root,
            width=25,
            font=("Arial", 28),
            highlightthickness=0,
            borderwidth=0
        )
        entry.bind("<Return>", lambda event: display_fortune())
        
        # Function to reset the GUI after showing the fortune
        def reset_gui():
            result_label.place_forget()
            result_label.config(text="")
            entry.delete(0, tk.END)

        def display_fortune():
            """Gets the fortune and updates the result label."""
            user_question = entry.get()
            fortune = get_fortune(user_question)
            # Show the label
            result_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
            result_label.config(text=fortune)

            root.after(12000, reset_gui)  # Reset everything to its initial state

        fortune_button = tk.Button(
            root,
            text="Prengúntale a Zoltar y presiona Enter",
            command=display_fortune,
            font=("Arial", 14, "bold"),
            bg="#4a90e2",
            fg="white",
            padx=20,
            pady=10,
            highlightthickness=0,
            borderwidth=0
        )

        result_label = tk.Label(
            root,
            text="",
            wraplength=520,
            font=("Arial", 16),
            bg="white",
            relief="sunken",
            padx=10,
            pady=10,
            highlightthickness=0,
            borderwidth=0
        )
        # Place widgets on the canvas with better spacing
        result_label.place_forget()        
        entry.place(relx=0.5, rely=0.78, anchor=tk.CENTER)
        fortune_button.place(relx=0.5, rely=0.84, anchor=tk.CENTER)
        
        # Set the background color of the root window to black
        root.configure(bg="#000000")

        # Bind the double click event to the canvas
        def toggle_fullscreen(event):
            """Toggles fullscreen mode."""
            if root.attributes("-fullscreen"):
                root.attributes("-fullscreen", False)
            else:
                root.attributes("-fullscreen", True)

        canvas.bind("<Double-Button-1>", toggle_fullscreen)

        # Block Control, Alt, and Shift keys
        root.bind("<Control_L>", lambda event: "break")
        root.bind("<Control_R>", lambda event: "break")
        root.bind("<Alt_L>", lambda event: "break")
        root.bind("<Alt_R>", lambda event: "break")
        root.bind("<Shift_L>", lambda event: "break")
        root.bind("<Shift_R>", lambda event: "break")

    except FileNotFoundError:
        messagebox.showerror("Error", "Could not find the background image file!")
        # Create a basic layout without the background image
        title_label = tk.Label(root, text="Zoltar Fortune Teller", font=("Arial", 16), bg="#000000")
        title_label.pack(pady=20)
        entry.pack(pady=20)
        fortune_button.pack(pady=20)
        result_label.pack(pady=20)

    # Run the Tkinter main loop
    root.mainloop()

    # Stop the music when the window is closed
    pygame.mixer.music.stop()
    pygame.mixer.quit()

if __name__ == "__main__":
    create_gui()