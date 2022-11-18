import random, os
from pathlib import Path
from flask import Flask, send_file

app = Flask(__name__)

def random_image():
    """
    Return a random image from the ones in the static/ directory
    """
    img_dir = Path('./static/images')
    #img_list = os.listdir(img_dir)
    img_path = random.choice(list(img_dir.glob('*.png')))
    return img_path
@app.route('/images/paperboy.png')
def myapp():
    """
    Returns a random image directly through send_file
    """
    image = random_image()
    return send_file(image, mimetype='image/png')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8888)