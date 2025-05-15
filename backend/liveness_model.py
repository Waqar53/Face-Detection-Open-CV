import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("liveness.model") 

labels = ['fake', 'real']

def preprocess_face(image):
    resized = cv2.resize(image, (32, 32)) 
    normalized = resized.astype("float") / 255.0
    return np.expand_dims(normalized, axis=0)

def is_live_face(frame):
    face = detect_face(frame)
    if face is None:
        return False  
    
    face_input = preprocess_face(face)
    preds = model.predict(face_input)[0]
    label = labels[np.argmax(preds)]
    print("Liveness:", label)
    return label == 'real'

def detect_face(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        return frame[y:y+h, x:x+w]
    
    return None