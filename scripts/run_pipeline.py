import cv2

from vision.yolo_detector import YOLODetector
from pipeline.scene_builder import build_scene
from reasoning.scene_reasoner import SceneReasoner


def main():

    image_path = "data/raw/test.jpg"

    detector = YOLODetector()
    reasoner = SceneReasoner()

    detections, image = detector.detect(image_path)

    print("\nDetections:")
    print(detections)

    scene = build_scene(detections)

    print("\nScene Understanding:")
    print(scene)

    reasoning = reasoner.reason(scene)

    print("\nLLM Reasoning:")
    print(reasoning)

    risk = reasoning["risk_level"].upper()
    action = reasoning["recommended_action"]

    panel_height = 140

    cv2.rectangle(
        image,
        (0, 0),
        (image.shape[1], panel_height),
        (0, 0, 0),
        -1
    )

    cv2.putText(
        image,
        f"RISK LEVEL: {risk}",
        (30, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.8,
        (0, 0, 255),
        4
    )

    cv2.putText(
        image,
        f"ACTION: {action}",
        (30, 110),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.1,
        (255, 255, 255),
        3
    )

    output_path = "data/processed/final_decision.jpg"

    cv2.imwrite(output_path, image)

    print("\nFinal image saved to:", output_path)


if __name__ == "__main__":
    main() 