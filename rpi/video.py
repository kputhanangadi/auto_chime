import cv2
import pathlib
import os
import uuid
import sys
import traceback

# Open the webcam
cap = cv2.VideoCapture(0)
# Get current dir
dir = pathlib.Path(__file__).parent.resolve()
POS_PATH = "./pos"

# make the pos directory if it doesn't exist
os.makedirs(POS_PATH, exist_ok=True) 

while True:
    # Read frame from the webcam
    ret, frame = cap.read()

    # Perform your image processing or machine learning tasks on the frame here
    if cv2.waitKey(1) & 0xFF == ord("p"):
        imgname = os.path.join(POS_PATH, "{}.jpg".format(uuid.uuid1()))
        print(f"writing to {imgname}")
        try:
            success = cv2.imwrite(imgname, frame)
            print(success)
        except Exception:
            print("Error during image write:")
            traceback.print_exc()

    # Display the frame
    cv2.imshow("Frame", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the webcam and close any open windows
cap.release()
cv2.destroyAllWindows()
