import cv2
import pathlib
import os

# Open the webcam
cap = cv2.VideoCapture(0)


# returns the current frame from the webcam. either a 3d numpy array or None
def main():
    ret, frame = cap.read()
    if ret:
        return frame
    else:
        return None
