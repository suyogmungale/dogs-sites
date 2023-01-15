from flask import Flask, render_template
import os, random

app = Flask(__name__)

@app.route('/')
def index():
    # Get a list of all JPG files in the "static" folder
    img_files = [f for f in os.listdir('/static') if f.endswith('.jpg')]
    # Select a random file from the list
    random_img = random.choice(img_files)
    # Render the "index.html" template and pass in the random image file name
    return render_template('index.html', random_img=random_img)

if __name__ == '__main__':
    app.run()
