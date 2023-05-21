import base64
from flask import Flask, request
from deepface import DeepFace
from PIL import Image
import io

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    data = request.get_json()
    base64_image = data['image']

    image_data = base64.b64decode(base64_image)
    image = Image.open(io.BytesIO(image_data))

    result = DeepFace.analyze(img_path = image, actions = ['emotion'])

    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)