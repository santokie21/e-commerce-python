from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from utils import detect_objects_in_image
import os

app = Flask(__name__)

@app.route('/upload-image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        tmp_dir = os.path.join(os.getcwd(), 'tmp')  # Adjusted to use the current working directory
        os.makedirs(tmp_dir, exist_ok=True)
        filename = secure_filename(file.filename)
        filepath = os.path.join(tmp_dir, filename)
        file.save(filepath)
        detected_classes = detect_objects_in_image(filepath)
        return detected_classes

if __name__ == '__main__':
    app.run(debug=True)
