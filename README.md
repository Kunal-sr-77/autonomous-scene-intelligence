Autonomous Scene Intelligence 🚗🧠

Autonomous Scene Intelligence is an end-to-end AI system designed to simulate how an intelligent agent interprets visual environments and makes decisions. It combines computer vision, retrieval-based knowledge, and language model reasoning into a single pipeline.

────────────────────────────────

Overview

This project processes an input image and performs multi-stage analysis:

• Detects objects using YOLO
• Converts detections into structured scene data
• Retrieves relevant safety rules using a lightweight RAG system
• Generates risk assessment and driving decisions using an LLM
• Exposes the entire pipeline through a FastAPI service

The system is built to reflect how autonomous systems move from perception to reasoning to action.

────────────────────────────────

Key Features

• Real-time object detection using YOLOv8
• Scene understanding through structured abstraction
• Retrieval-Augmented Generation (RAG) for rule grounding
• LLM-based reasoning for risk and action decisions
• REST API for easy integration and testing
• Annotated outputs for interpretability

────────────────────────────────

Technology Stack

• Python
• FastAPI
• Ultralytics YOLOv8
• OpenRouter (LLM inference)
• OpenCV
• Custom RAG pipeline

────────────────────────────────

Project Structure

autonomous-scene-intelligence/

api/ → FastAPI backend
vision/ → Object detection and visualization
pipeline/ → Scene construction and orchestration
reasoning/ → Prompting and LLM interaction
rag/ → Retrieval logic and knowledge base
evaluation/ → Metrics and validation
scripts/ → Execution entry points
configs/ → Configuration files
requirements.txt → Dependencies

────────────────────────────────

System Workflow

1. Input image is provided to the system
2. YOLO detects objects such as pedestrians and vehicles
3. Scene builder converts detections into structured representation
4. RAG module retrieves relevant safety rules
5. LLM generates:
   • Scene description
   • Risk level
   • Main risk
   • Recommended action

────────────────────────────────

API Usage

Endpoint
POST /analyze_scene

Request
Upload an image file

Response (example)

{
"detections": [...],
"scene": {...},
"decision": {
"risk_level": "medium",
"recommended_action": "Reduce speed and prepare to brake"
}
}

Swagger UI available at:
http://localhost:8000/docs

────────────────────────────────

Running Locally

Install dependencies:

pip install -r requirements.txt

Start the server:

uvicorn api.app:app --reload

────────────────────────────────

Deployment

The application is deployed using Render as a cloud-based FastAPI service.

────────────────────────────────

Key Learnings

• Integration of computer vision and language models
• Designing modular AI pipelines
• Applying RAG to reduce hallucinations
• Handling real-world constraints such as memory and performance
• Building deployable AI APIs

────────────────────────────────

Future Improvements

• Improve detection accuracy and filtering
• Enhance visualization and UI clarity
• Support real-time video streams
• Upgrade RAG with vector databases
• Optimize for edge deployment

────────────────────────────────

Author

Kunal
B.Tech Computer Science (AI/ML)

────────────────────────────────

License

This project is intended for educational and research purposes.
