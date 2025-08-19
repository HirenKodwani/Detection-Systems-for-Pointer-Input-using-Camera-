import cv2
import numpy as np
import pyautogui
from ultralytics import YOLO
import time

# Initialize webcam
cap = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()

# Load YOLOv8 hand detection model
model = YOLO("C:/Users/ADMIN/Downloads/hand_yolov8n.pt")

# Smooth movement using moving average
prev_x, prev_y = 0,0
alpha = 0.3  # Smoothing factor (0 = full smooth, 1 = no smooth)

# For click gesture
click_threshold = 100  # Min size to avoid clicking
click_cooldown = 1  # seconds
last_click_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    results = model.predict(source=frame, imgsz=320, conf=0.6, device='cpu', verbose=False)
    detections = results[0].boxes.data

    if len(detections) > 0:
        for det in detections:
            x1, y1, x2, y2, conf, cls = det
            x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))

            # Calculate center of bounding box
            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)

            # Map webcam coords to screen coords
            screen_x = np.interp(cx, [0, frame.shape[1]], [0, screen_w])
            screen_y = np.interp(cy, [0, frame.shape[0]], [0, screen_h])

            # Smooth the movement
            smooth_x = int(prev_x + alpha * (screen_x - prev_x))
            smooth_y = int(prev_y + alpha * (screen_y - prev_y))
            pyautogui.moveTo(smooth_x, smooth_y)
            prev_x, prev_y = smooth_x, smooth_y

            # Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Gesture click (when hand gets small enough = close fingers)
            box_width = x2 - x1
            box_height = y2 - y1
            box_area = box_width * box_height

            if box_area < click_threshold * click_threshold:
                if time.time() - last_click_time > click_cooldown:
                    pyautogui.click()
                    last_click_time = time.time()
                    print("Click!")

    cv2.imshow("Hand Tracking", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()