# Autonomous Scene Intelligence

Perception-to-decision AI system that combines computer vision, retrieval-based reasoning, and large language models to generate structured driving decisions from real-world scenes.

---

## Highlights

* Built end-to-end perception-to-decision pipeline using **YOLOv8 + RAG + LLM**
* Integrated retrieval-based safety rules to improve reliability of model outputs
* Generated structured decisions: scene description, risk level, and recommended action
* Deployed system via **FastAPI** for real-time scene analysis
* Designed modular architecture for integrating perception and reasoning systems

---

## Problem Statement

Autonomous driving systems require accurate perception and reliable decision-making.
While computer vision models can detect objects, they lack contextual reasoning, and LLMs alone may produce unsafe or hallucinated outputs.

Key challenges:

* Converting raw visual detections into meaningful scene understanding
* Ensuring reasoning is grounded in safety constraints
* Generating actionable and interpretable driving decisions

---

## Solution Overview

This project implements a perception-to-decision pipeline that:

* Detects objects in real-world scenes using YOLOv8
* Converts detections into structured scene representations
* Retrieves relevant safety rules using a rule-based RAG system
* Uses an LLM to generate risk-aware decisions
* Exposes the pipeline via a FastAPI service

---

## System Architecture

Input Image
→ Object Detection (YOLOv8)
→ Scene Representation
→ Retrieval Layer (Safety Rules via RAG)
→ LLM Reasoning
→ Decision Output (Description, Risk, Action)
→ API Response

---

## Key Insight

Retrieval-based grounding significantly improves the reliability of LLM-generated decisions in safety-critical scenarios by reducing hallucinated or unsafe recommendations.

---

## Features

### Object Detection

Detects entities such as pedestrians and vehicles using YOLOv8.

### Scene Representation

Transforms raw detections into structured semantic data.

### Retrieval-Augmented Reasoning

Incorporates predefined safety rules to guide model outputs.

### Decision Generation

Produces:

* Scene description
* Risk level
* Recommended action

### API Interface

Exposes functionality through a FastAPI-based service.

### Visualization

Generates annotated outputs with bounding boxes and decision overlays.

---

## API Usage

### Endpoint

POST `/analyze_scene`

### Input

Upload an image file via `multipart/form-data`.

### Output

* detected objects
* structured scene representation
* decision (risk level and recommended action)

---

## Typical Flow

1. Image is submitted to the API
2. Objects are detected using YOLOv8
3. Scene is structured into a semantic representation
4. Relevant safety rules are retrieved
5. LLM generates risk assessment and action

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Kunal-sr-77/autonomous-scene-intelligence.git
cd autonomous-scene-intelligence
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Set Environment Variables

```bash
touch .env
echo "OPENROUTER_API_KEY=your_api_key" >> .env
```

---

## Running the System

```bash
uvicorn api.app:app --reload
```

Access API documentation:
http://127.0.0.1:8000/docs

---

## Tech Stack

### Backend

* FastAPI
* Python

### Computer Vision

* Ultralytics YOLOv8

### Reasoning

* OpenRouter (LLM inference)

### Retrieval

* Custom rule-based RAG

### Visualization

* OpenCV

---

## Why This Matters

Autonomous systems require both perception and reasoning to operate safely.
This project demonstrates how visual understanding can be combined with retrieval-based grounding and LLM reasoning to produce actionable and safer driving decisions.

This forms the foundation for building reliable and interpretable AI systems in autonomous driving.

---

## Key Learnings

* Designing modular AI pipelines combining CV and LLMs
* Integrating retrieval-based grounding to reduce hallucination
* Converting perception outputs into structured reasoning inputs
* Building deployable AI systems with FastAPI
* Handling real-world constraints such as performance and modularity

---

## Future Improvements

* Improve detection precision and filtering
* Support real-time video input and streaming inference
* Integrate vector-based retrieval systems
* Enhance decision validation and evaluation (extended in Project 2)
* Optimize performance for edge deployment

---
