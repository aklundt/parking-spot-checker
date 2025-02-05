import time

import cv2 as cv
from ultralytics import YOLO


def draw_circles(given_img, detected_id, conf, xyxy, size):
    x1, y1, x2, y2 = map(int, xyxy)
    center = (x1 + (x2 - x1) // 2, y1 + (y2 - y1) // 2)
    if conf > confidence_threshold:
        if detected_id == 0:
            cv.circle(given_img, center, int(size * min(x2 - x1, y2 - y1)), (64, 64, 255), -1)
        else:
            cv.circle(given_img, center, int(size * min(x2 - x1, y2 - y1)), (102, 255, 64), -1)
    return given_img


# Define constants
model_path = 'models/best_320x12n.pt'
confidence_threshold = 0.35
dot_size = 0.10
# URL of the stream provided by running stream_mjpeg.py
stream_url = 'http://localhost:8080/parking_lot'
process_interval = 10  # seconds

# Load stream
cap = cv.VideoCapture(stream_url)

if not cap.isOpened():
    print("Error: Could not open video stream")
    exit()

# Load YOLOv8 model
model = YOLO(model_path)

while True:
    read_successfully, frame = cap.read()
    if not read_successfully:
        print("Error: Could not read frame")
        break

    height, width = frame.shape[:2]

    # Perform inference
    results = model.predict(frame, conf=0.01)

    # Render and display inference
    for result in results:
        for box in result.boxes:
            confidence = box.conf[0].item()
            class_id = int(box.cls[0])
            frame = draw_circles(frame, class_id, confidence, box.xyxy[0], dot_size)

    frame = cv.resize(frame, (640, int(640 * height / width)))
    cv.imshow(f'Inferenced Stream at 1 frame every {process_interval} seconds', frame)

    # Controls to increase and decrease dot size
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('w'):
        dot_size = dot_size + 0.05
    elif key == ord('s'):
        if dot_size > 0.05:
            dot_size = dot_size - 0.05
    time.sleep(process_interval)

cap.release()
cv.destroyAllWindows()
