import cv2
import mediapipe as mp

def detect_facial_movement():
    cap = cv2.VideoCapture(0)
    mp_face_mesh = mp.solutions.face_mesh.FaceMesh()

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break

        # Flip the image horizontally for a later selfie-view display
        image = cv2.flip(image, 1)
        results = mp_face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # Example: Detect blink by checking specific landmarks
                print(face_landmarks.landmark[0])

        cv2.imshow('Facial Movement Detection', image)

        if cv2.waitKey(5) & 0xFF == 27:  # Press 'Esc' to exit
            break

    cap.release()
    cv2.destroyAllWindows()
