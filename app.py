from flask import Flask, request
from flask_cors import CORS, cross_origin
from deepface import DeepFace

app = Flask("face_recognition")

cors = CORS(app)

@cross_origin()
@app.route('/', methods=['GET'])
def index():
    return 'hi'

@cross_origin()
@app.route('/ai/example', methods=['POST'])
def upload_file():
    try:
        image_data = request.form.get('image')
        result = DeepFace.analyze(img_path=image_data, actions=['emotion'])
        print(result)

        return result[0]['dominant_emotion']

    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
