import cv2
import tkinter as tk
from tkinter import filedialog

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Can't read the image. Image path:", image_path)
        return

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('None', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def select_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if file_path:
        print("Selected Image Path:", file_path)
        detect_faces(file_path)

select_image()