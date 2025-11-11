# Pothole Patrol AI
**Real-time pothole detection for safer roads & smarter fleets**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-red?logo=streamlit&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-ONNX-success?logo=ultralytics)
![AWS](https://img.shields.io/badge/Deployed%20on-AWS%20Lightsail-orange?logo=amazonaws)

**Live App (mobile camera works):** [https://pothole-patrol-ai.com](https://pothole-patrol-ai.com)

---

## Overview

**Pothole Patrol AI** is a **real-time computer vision web app** that uses **YOLOv8 (ONNX)** to detect potholes via **four powerful input modes**:

- **Upload your own image** — Drag and drop any road photo  
- **Live phone camera** — Point and detect in real time  
- **Preloaded examples** — Try 5 built-in pothole samples  
- **Video demo** — Watch AI analyze real driving footage  

Built for **fleet managers, city officials, and drivers**, it instantly identifies road hazards and simulates reporting to a **SmartFleet dashboard** for optimized repair routing.

---

## Key Features

### Live Camera Detection  
Point your phone at the road — AI highlights potholes instantly.

![Live Camera Detection](screenshots/camera-detection.png)  
*Phone camera view with blue bounding boxes and confidence scores.*

---

### Image Upload & Preloaded Examples  
Upload any photo or try 5 preloaded pothole samples.

![Upload Detection](screenshots/upload-detection.png)  
*Example image with detected potholes and confidence labels.*

---

### SmartFleet Reporting (Demo)  
Tap **Report To SmartFleet** — simulates sending the image + fake GPS to the fleet system.

![Report Success](screenshots/report-success.png)  
*Success message with fake Chicago coordinates, balloons, and SmartFleet link.*

---

### Video Demo  
Watch AI in action on real driving footage.

![Video Demo](screenshots/video-demo.png)  
*Video player paused on a frame with pothole detection.*

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| **YOLOv8 (ONNX)** | Ultra-fast pothole detection model |
| **ONNX Runtime** | Lightweight inference engine |
| **Streamlit** | Interactive web frontend |
| **OpenCV** | Image preprocessing & bounding box rendering |
| **AWS Lightsail** | Production hosting |
| **AWS S3** | Report storage (future analytics) |
| **Python 3.9+** | Core language |

---

## How It Works

```mermaid
graph TD
    A[User opens app] --> B{Choose input}
    B --> C[Upload Photo]
    B --> D[Use Phone Camera]
    B --> E[Select Example]
    B --> F[Watch Video Demo]
    C --> G[Preprocess → 640x640]
    D --> G
    E --> G
    F --> H[Play Pre-recorded Video]
    G --> I[ONNX Model Inference]
    I --> J[Post-process + NMS]
    J --> K[Draw Blue Boxes + Confidence]
    K --> L{Report?}
    L -->|Yes| M[Fake GPS + Success + Balloons]
    L -->|No| N[View Results]
