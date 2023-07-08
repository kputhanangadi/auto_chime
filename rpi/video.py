import cv2
import pathlib
import os

# Open the webcam
cap = cv2.VideoCapture(0)
# Get current dir
dir = pathlib.Path(__file__).parent.resolve()
POS_PATH = "./pos"

# make the pos directory if it doesn't exist
os.makedirs(POS_PATH, exist_ok=True)


# returns the current frame from the webcam. either a 3d numpy array or None
def main():
    ret, frame = cap.read()
    if ret:
        return frame
    else:
        return None
