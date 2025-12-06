import sys
import os
from PIL import Image

# Function to get the absolute path to a resource (handles both development and PyInstaller's bundle)
def resource_path(relative_path):
    """ Get the absolute path to a resource, works for dev and for PyInstaller's bundled files """
    try:
        # PyInstaller creates a temporary folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Load bus final image
bus_image_path = resource_path("bus final image.jpg")
bus_image = Image.open(bus_image_path)

# Load vasavi firstpage image
vasavi_image_path = resource_path("vasavi firstpage.jpg")
vasavi_image = Image.open(vasavi_image_path)

# Example usage: You can set the background with one of the images
background_image = bus_image  # or use vasavi_image depending on your application logic

# Flask part for the web interface
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to download the application (assumes titlepage.exe is in 'dist' folder)
@app.route('/download')
def download():
    dist_folder = os.path.join(app.root_path, 'dist')
    return send_from_directory(directory=dist_folder, path='titlepage.exe', as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
