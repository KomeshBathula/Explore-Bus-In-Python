import tkinter as tk
from PIL import Image, ImageTk
import sys
import os
import subprocess
import random

def launch_first_program():
    # Always run the Python script for firstpage.py, regardless of whether it's in script or application mode
    firstpage_py = os.path.join(os.path.dirname(os.path.abspath(__file__)), "firstpage.py")
    subprocess.Popen(["python", firstpage_py], shell=True)

# Function to get the absolute path for bundled resources
def resource_path(relative_path):
    """ Get the absolute path to a resource, works for dev and for PyInstaller's bundled files """
    try:
        # PyInstaller creates a temporary folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Create the main window
root = tk.Tk()
root.title("Explore Bus")
root.attributes('-fullscreen', True)

background_images = [
    "firstpage bus image.jpg",
    "bus final image.jpg",
    "bus final image1.jpg"
]

# Load and set the background image using resource_path
selected_image = random.choice(background_images)
bus_image_path = resource_path(selected_image)
bus_image = Image.open(bus_image_path)
bus_image = bus_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
bg_image = ImageTk.PhotoImage(bus_image)

# Create a label for displaying the background image
background_label = tk.Label(root, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.image = bg_image  # Prevent garbage collection

# Create a label for the title
title_label = tk.Label(root, text="Explore Bus", font=("Arial", 80, "bold"), fg="#FFFFFF", bg="#FF4500")
title_label.pack(pady=20, anchor=tk.CENTER)

# Button styling
button_style = {
    "font": ("Arial", 20, "bold"),
    "bg": "#32CD32",  # Lime Green
    "fg": "#FFFFFF",  # White text
    "activebackground": "#1E90FF",  # Dodger Blue on hover
    "activeforeground": "#FFFFFF",
    "relief": tk.RAISED,
    "bd": 5,
    "width": 20,
    "highlightthickness": 2,
    "highlightbackground": "#FF4500",
    "highlightcolor": "#FF4500",
}

# Create a button to go to the main page
main_page_button = tk.Button(root, text="Begin Search", command=launch_first_program, **button_style)
main_page_button.pack(pady=30)

# Create an exit button
exit_button = tk.Button(root, text="EXIT", command=root.quit, **button_style)
exit_button.pack(pady=30)

# Create a label for the team text at the bottom center of the window
team_label = tk.Label(root, text="By Team A - 11", font=("Arial", 25), fg="#FFFFFF", bg="#FF4500")
team_label.pack(side=tk.BOTTOM, pady=10, anchor=tk.CENTER)

# Start the Tkinter event loop
root.mainloop()
