import time
import cv2 as cv
from sahi import AutoDetectionModel
from sahi.predict import get_sliced_prediction
from ultralytics import YOLO


def draw_circles(given_img, detected_id, conf, xyxy):
    x1, y1, x2, y2 = map(int, xyxy)
    center = (x1 + (x2 - x1) // 2, y1 + (y2 - y1) // 2)
    if conf > confidence_threshold:
        if detected_id == 0:
            cv.circle(given_img, center, int(dot_size * min(x2-x1, y2-y1)), (64, 64, 255), -1)
        else:
            cv.circle(given_img, center, int(dot_size * min(x2-x1, y2-y1)), (102, 255, 64), -1)
    return given_img

# Define constants
model_path = 'models/best_50x8.pt'
img_path = 'tests/testies2.jpg'
confidence_threshold = 0.35
slice_size = 400
overlap_ratio = 0.2
dot_size = 0.35

# Load image
img = cv.imread(img_path)
height, width = img.shape[:2]
print(f'Image shape: {img.shape}')

# Load YOLOv8 and SAHI models
regular_model = YOLO(model_path)

sahi_model = AutoDetectionModel.from_pretrained(
    model_type="yolov8",
    model_path=model_path,
    confidence_threshold=0.01,
    device="cuda:0",
)

# Perform inferences
start_time = time.time()
sahi_result = get_sliced_prediction(
    img,
    sahi_model,
    slice_height=slice_size,
    slice_width=slice_size,
    overlap_height_ratio=overlap_ratio,
    overlap_width_ratio=overlap_ratio,
)
end_time = time.time()
print(f'SAHI inference time: {end_time - start_time:.2f} seconds')

regular_results = regular_model.predict(img, conf=0.01)

while True:
    sahi_img = img.copy()
    regular_img = img.copy()

    # Render and display SAHI inference
    for result in sahi_result.object_prediction_list:
        confidence = result.score.value
        class_id = result.category.id
        sahi_img = draw_circles(sahi_img, class_id, confidence, result.bbox.to_xyxy())

    sahi_img = cv.resize(sahi_img, (640, int(640 * height / width)))
    cv.imshow('SAHI Inference', sahi_img)

    # Render and display regular inference
    for result in regular_results:
        for box in result.boxes:
            confidence = box.conf[0].item()
            class_id = int(box.cls[0])
            regular_img = draw_circles(regular_img, class_id, confidence, box.xyxy[0])

    regular_img = cv.resize(regular_img, (640, int(640 * height / width)))
    cv.imshow('Regular Inference', regular_img)

    # Controls to increase and decrease dot size
    key = cv.waitKey(100) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('w'):
        dot_size = dot_size + 0.05
    elif key == ord('s'):
        if dot_size > 0.05:
            dot_size = dot_size - 0.05

cv.destroyAllWindows()

print("SAHI is pretty bad in this situation, no matter how I configure it. I'm not sure why. It's slower and less accurate than the regular YOLOv8 model.")