import cv2


def draw_boxes(image, detections):

    for det in detections:

        x1, y1, x2, y2 = det["bbox"]
        label = det["label"]
        conf = det["confidence"]

        text = f"{label} {conf:.2f}"

        # thick bounding box
        cv2.rectangle(
            image,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            4
        )

        (tw, th), _ = cv2.getTextSize(
            text,
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            2
        )

        # label background
        cv2.rectangle(
            image,
            (x1, y1 - th - 10),
            (x1 + tw + 10, y1),
            (0, 255, 0),
            -1
        )

        cv2.putText(
            image,
            text,
            (x1 + 5, y1 - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 0),
            2
        )

    return image


def draw_decision_overlay(image, reasoning):

    risk = reasoning["risk_level"].upper()
    action = reasoning["recommended_action"]

    h, w = image.shape[:2]

    panel_height = 200

    cv2.rectangle(
        image,
        (0, 0),
        (w, panel_height),
        (30, 30, 30),
        -1
    )

    cv2.putText(
        image,
        f"RISK LEVEL: {risk}",
        (30, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        2.2,
        (0, 0, 255),
        6
    )

    cv2.putText(
        image,
        "ACTION:",
        (30, 150),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.4,
        (255, 255, 255),
        3
    )

    cv2.putText(
        image,
        action,
        (200, 150),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.3,
        (255, 255, 255),
        3
    )

    return image 