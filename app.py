from flask import Flask, request
from flask_cors import CORS, cross_origin
from deepface import DeepFace
from PIL import Image
import os
import time

app = Flask(__name__)

cors = CORS(app)

@cross_origin
@app.route('/', methods=['GET'])
def index():
    return 'hi'

def safe_remove(filename):
    while True:
        try:
            os.remove(filename)
            break
        except PermissionError:
            time.sleep(0.1)

@cross_origin
@app.route('/predict', methods=['POST'])
def upload_file():
    try:
        image_data = request.form.get('image')
        # image_decoded = base64.b64decode(image_data)
        # image = Image.open(io.BytesIO(image_decoded))

        # _, temp_filename = tempfile.mkstemp(suffix=".jpg")
        # image.save(temp_filename, "JPEG")

        # logger.debug("Analyzing image with DeepFace...")
        result = DeepFace.analyze(img_path=image_data, actions=['emotion'])
        print(result)

        # safe_remove(temp_filename)

        # gc.collect()  # Manually trigger garbage collection

        return result[0]['dominant_emotion']

    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
