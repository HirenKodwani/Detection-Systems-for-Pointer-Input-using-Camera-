# Detection-Systems-for-Pointer-Input-using-Camera-
This repository contains two Python-based computer vision projects designed to enable hands-free accessibility and interaction with computers. Both algorithms leverage the webcam for real-time tracking and control, making them suitable for people with limited mobility or those who want gesture-based input.



This system uses YOLOv8 (a deep learning object detection model) to detect and track the user’s hand in real time. The hand’s position is mapped to the mouse pointer, allowing users to move the cursor simply by moving their hand in front of the camera.

A gesture-based click is also implemented:

When the bounding box size of the hand gets small (fingers closed), the system interprets it as a mouse click.

Movement smoothing is applied to make cursor control natural and less jittery.

Key Features

Real-time hand tracking using YOLOv8.

Smooth pointer movement mapped from camera to screen.

Gesture-based mouse click detection.

Useful for accessibility, presentations, or gesture-driven applications.

2. Color-Based Pointer Control (Marker/Glove Tracking)
Description

This system uses color detection in HSV space to track a colored object (e.g., a green marker, glove, or sticker). The centroid of the detected color region is mapped to the mouse pointer, allowing intuitive cursor control.

Unlike AI detection, this approach is lightweight and does not require pre-trained models — making it efficient on low-resource machines.

Key Features

Tracks a specific color object (default: green, but customizable).

Maps movement of the object to mouse pointer control.

Lightweight and fast — works without deep learning models.

Adjustable HSV ranges for different colors.

Accessibility Impact

These projects can help:

People with limited mobility use computers through hand gestures or color markers.

Developers create gesture-driven applications and prototypes.

Educators and presenters demonstrate hands-free interaction.

Notes

For better performance, ensure proper lighting conditions.

Adjust HSV color ranges in the color-based script to match your marker/glove color.

For YOLO-based tracking, GPU acceleration (if available) will significantly improve performance.
