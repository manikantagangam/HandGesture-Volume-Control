import cv2
import mediapipe as mp
import numpy as np
import os
import tkinter as tk
from PIL import Image, ImageTk
from math import hypot

# Initialize Mediapipe Hands module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Initialize volume bar and percentage variables
volbar = 400
volper = 0

# Function to set system volume on macOS
def set_system_volume(volume):
    volume_level = int(round(volume))
    command = f"osascript -e 'set volume output volume {volume_level}'"
    os.system(command)

# Function to update the volume based on hand coordinates and length
def update_volume(x1, y1, length):
    global volper, volbar
    volper = np.interp(length, [30, 350], [0, 100])
    set_system_volume(volper)
    volbar = int(np.interp(length, [30, 350], [400, 150]))
    canvas.coords(volume_bar, x1, y1, x1 + 35, volbar)
    volume_label.config(text=f"{int(volper)}%")

# Function to process images, detect hand landmarks and update volume
def process_image(img):
    global volbar, volper
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    lmList = []
    if results.multi_hand_landmarks:
        for handlandmark in results.multi_hand_landmarks:
            for id, lm in enumerate(handlandmark.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
            mpDraw.draw_landmarks(img, handlandmark, mpHands.HAND_CONNECTIONS)

    # Calculate hand coordinates and distance between two landmarks
    x1, y1 = 0, 0
    if lmList != []:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cv2.circle(img, (x1, y1), 13, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 13, (255, 0, 0), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
        length = hypot(x2 - x1, y2 - y1)
        update_volume(x1, y1, length)

    return img, x1, y1

# Function to update the video stream continuously
def update_video_stream():
    global canvas, video_stream, cap
    
    ret, frame = cap.read()
    if ret:
        img, x1, y1 = process_image(frame)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = img.resize((640, 480), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)
        canvas.itemconfig(video_stream, image=img_tk)
        canvas.image = img_tk

    root.after(15, update_video_stream)

# Initialize webcam capture
cap = cv2.VideoCapture(0)

# Set up tkinter GUI
root = tk.Tk()
root.title("Hand Gesture Volume Control")
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# Create tkinter GUI elements
video_stream = canvas.create_image(10, 10, anchor=tk.NW)
volume_bar = canvas.create_rectangle(50, 150, 85, 400, fill="red")
volume_label = tk.Label(root, text="0%", font=("Helvetica", 36))
volume_label.pack()

# Start updating the video stream
update_video_stream()
root.mainloop()

# Release resources
cap.release()
cv2.destroyAllWindows()