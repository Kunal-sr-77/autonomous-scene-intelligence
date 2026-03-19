# Autonomous Scene Intelligence

A modular AI system that combines computer vision, retrieval-based knowledge, and language model reasoning to analyze real-world scenes and generate actionable decisions.  
Designed as a perception-to-decision pipeline for autonomous and intelligent systems.

---

## Features

### Object Detection  
Detects entities such as pedestrians and vehicles using YOLOv8.

### Scene Representation  
Transforms raw detections into structured scene data.

### Retrieval-Augmented Reasoning  
Incorporates predefined safety rules to ground model outputs.

### Decision Generation  
Produces scene descriptions, risk levels, and recommended actions using an LLM.

### API Interface  
Exposes functionality through a FastAPI-based service.

### Annotated Outputs  
Generates visual results with bounding boxes and decision overlays.

---

## Quick Start

### Prerequisites

- Python 3.10 or higher  
- OpenRouter API key  

---

### Installation

```bash
git clone https://github.com/Kunal-sr-77/autonomous-scene-intelligence.git
cd autonomous-scene-intelligence
pip install -r requirements.txt
```

---

### Run the Application

```bash
uvicorn api.app:app --reload
```

---

### Access the API

```
http://127.0.0.1:8000/docs
```

---

## Usage

### Endpoint

```bash
POST /analyze_scene
```

### Input

Upload an image file via `multipart/form-data`.

### Output

- detections  
- scene representation  
- decision (risk level and recommended action)  

---

## Typical Flow

1. Image is submitted to the API  
2. Objects are detected using YOLOv8  
3. Scene is structured into a semantic representation  
4. Relevant rules are retrieved via RAG  
5. LLM generates risk assessment and action  

---

## Architecture

### System Pipeline

```
Input Image
→ Object Detection (YOLOv8)
→ Scene Builder
→ Retrieval Layer (RAG)
→ LLM Reasoning
→ API Response
```

---

## Technology Stack

### Backend
- FastAPI  
- Python  

### Computer Vision
- Ultralytics YOLOv8  

### Reasoning
- OpenRouter (LLM inference)  

### Retrieval
- Custom rule-based RAG  

### Visualization
- OpenCV  

---

## Project Structure

```
autonomous-scene-intelligence/

api/                FastAPI service  
vision/             Detection and visualization  
pipeline/           Scene construction logic  
reasoning/          Prompting and LLM interface  
rag/                Retrieval system  
evaluation/         Metrics and validation  
scripts/            Execution entry points  
configs/            Configuration files  
requirements.txt    Dependencies  
```

---

## Development

### Run Pipeline Directly

```bash
python -m scripts.run_pipeline
```

---

### Test API Locally

```
http://127.0.0.1:8000/docs
```

---

## Configuration

### Environment Variables

```bash
OPENROUTER_API_KEY=your_api_key
```

Ensure the key is configured before running the service.

---

## Deployment

Designed for deployment on Render as a FastAPI service.

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
uvicorn api.app:app --host 0.0.0.0 --port 10000
```

---

## Key Learnings

- Designing modular AI pipelines  
- Integrating perception, retrieval, and reasoning systems  
- Applying retrieval-based grounding to reduce hallucination  
- Handling real-world constraints such as memory and latency  
- Building deployable AI services  

---

## Future Improvements

- Improve detection precision and filtering  
- Enhance visualization clarity  
- Support real-time video inputs  
- Integrate vector-based retrieval systems  
- Optimize performance for edge environments  


