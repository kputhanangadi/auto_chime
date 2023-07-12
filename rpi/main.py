import threading

from keras.models import load_model
from video import main as video
from chime import main as chime

MODEL_PATH = "../models/traffic_detection.h5"


def run_model():
    # Load model
    model = load_model(MODEL_PATH)

    # Get video frame
    frame = video()

    # Make prediction
    prediction = model.predict(frame)

    # Play chime if prediction is true
    if prediction:
        chime()


def main():
    # Setup a timer to check video every 2 seconds
    threading.Timer(2.0, run_model).start()


if __name__ == "__main__":
    main()
