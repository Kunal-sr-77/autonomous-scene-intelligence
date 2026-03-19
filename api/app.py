from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from vision.visualizer import draw_boxes, draw_decision_overlay
import shutil
import os
import cv2

from vision.yolo_detector import YOLODetector
from pipeline.scene_builder import build_scene
from reasoning.scene_reasoner import SceneReasoner
from vision.visualizer import draw_decision_overlay


app = FastAPI(title="Autonomous Scene Intelligence API")

detector = YOLODetector()
reasoner = SceneReasoner()


@app.post("/analyze_scene")
async def analyze_scene(file: UploadFile = File(...)):

    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)

    image_path = f"data/raw/{file.filename}"

    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    detections, image = detector.detect(image_path)

    scene = build_scene(detections)

    reasoning = reasoner.reason(scene)
    image = draw_boxes(image, detections)
    image = draw_decision_overlay(image, reasoning) 

    

    output_path = "data/processed/api_result.jpg"

    cv2.imwrite(output_path, image)

    return {
        "detections": detections,
        "scene": scene,
        "decision": reasoning,
        "annotated_image": output_path
    }
@app.get("/result_image")
def get_result_image():

    image_path = "data/processed/api_result.jpg"

    return FileResponse(
        image_path,
        media_type="image/jpeg",
        filename="result.jpg"
    ) 