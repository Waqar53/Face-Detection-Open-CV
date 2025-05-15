import face_recognition

# Load your known face encodings
known_faces = {
    "waqar": face_recognition.face_encodings(face_recognition.load_image_file("waqar.jpg"))[0]
}

def recognize_face(image):
    face_locations = face_recognition.face_locations(image)
    if not face_locations:
        return None

    face_encodings = face_recognition.face_encodings(image, face_locations)
    for face_encoding in face_encodings:
        for name, known_encoding in known_faces.items():
            matches = face_recognition.compare_faces([known_encoding], face_encoding)
            if matches[0]:
                return name
    return None