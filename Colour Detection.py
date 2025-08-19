import cv2
import numpy as np
import pyautogui

# Get screen size
screen_width, screen_height = pyautogui.size()

# Start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Camera width
cap.set(4, 480)  # Camera height

# Define color range for green (you can adjust this for other colors)
lower_color = np.array([40, 70, 70])
upper_color = np.array([80, 255, 255])

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Mirror image

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Find largest contour
        largest_contour = max(contours, key=cv2.contourArea)

        if cv2.contourArea(largest_contour) > 500:
            # Get bounding box
            x, y, w, h = cv2.boundingRect(largest_contour)
            center_x = x + w // 2
            center_y = y + h // 2

            # Map camera coords to screen coords
            screen_x = np.interp(center_x, [0, 640], [0, screen_width])
            screen_y = np.interp(center_y, [0, 480], [0, screen_height])

            # Move mouse
            pyautogui.moveTo(screen_x, screen_y)

            # Draw tracking box
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.circle(frame, (center_x, center_y), 5, (255, 0, 255), -1)

    # Show result
    cv2.imshow("Color-Based Pointer Control", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
