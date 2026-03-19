from ultralytics import YOLO
import cv2
import os


class YOLODetector:

    def __init__(self):
        self.model = YOLO("yolov8s.pt")  # auto-downloads if missing r
        self.device = "cpu"

        self.allowed_objects = {
            "person",
            "car",
            "truck",
            "bus",
            "bicycle",
            "motorcycle"
        }

    def detect(self, image_path):

        image = cv2.imread(image_path)
        img_h, img_w = image.shape[:2]

        results = self.model(image_path, device=self.device)

        detections = []

        for r in results:

            boxes = r.boxes

            for box in boxes:

                label = r.names[int(box.cls)]
                conf = float(box.conf)

                if conf < 0.4:
                    continue

                if label not in self.allowed_objects:
                    continue

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                box_w = x2 - x1
                box_h = y2 - y1

                if box_w > img_w * 0.9 or box_h > img_h * 0.9:
                    continue

                # Draw bounding box
                cv2.rectangle(
                    image,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    4
                )

                label_text = f"{label} {conf:.2f}"

                (tw, th), _ = cv2.getTextSize(
                    label_text,
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    2
                )

                # Label background
                cv2.rectangle(
                    image,
                    (x1, y1 - th - 10),
                    (x1 + tw + 6, y1),
                    (0, 255, 0),
                    -1
                )

                cv2.putText(
                    image,
                    label_text,
                    (x1 + 3, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 0, 0),
                    2
                )

                detections.append({ 
    "label": label,
    "confidence": round(conf, 3),
    "bbox": [x1, y1, x2, y2]
})

        os.makedirs("data/processed", exist_ok=True)

        cv2.imwrite("data/processed/detected_image.jpg", image)

        return detections, image