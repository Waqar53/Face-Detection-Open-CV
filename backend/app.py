from flask import Flask, request, jsonify
from liveness_model import is_live_face
from recognizer import recognize_face
import base64
import cv2
import numpy as np

app = Flask(__name__)

def decode_base64_image(data):
    content = base64.b64decode(data)
    nparr = np.frombuffer(content, np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

@app.route("/authenticate", methods=["POST"])
def authenticate():
    data = request.get_json()
    img_data = data.get("image")
    if not img_data:
        return jsonify({"success": False, "error": "No image provided"}), 400

    image = decode_base64_image(img_data)

    if not is_live_face(image):
        return jsonify({"success": False, "error": "Liveness check failed"}), 403

    user = recognize_face(image)
    if user:
        return jsonify({"success": True, "user": user})
    else:
        return jsonify({"success": False, "error": "Face not recognized"}), 404

if __name__ == "__main__":
    app.run(debug=True)