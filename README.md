# 🚧 Pothole Patrol AI  
**Real-time pothole detection for safer roads & smarter fleets**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-red?logo=streamlit&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-ONNX-success?logo=ultralytics)
![AWS](https://img.shields.io/badge/Deployed%20on-AWS%20Lightsail-orange?logo=amazonaws)

> **Live APP:** [https://pothole-patrol-ai.com](https://pothole-patrol-ai.com)  


---

## 📸 Screenshots

| Feature | Preview |
|--------|--------|
| **Main Dashboard** | ![App Hero](screenshots/hero.png) <!-- ADD: Full app view with title + 3 columns --> |
| **Pothole Detection (Upload)** | ![Upload Detection](screenshots/upload-detection.png) <!-- ADD: Image with blue boxes + confidence --> |
| **Live Camera Mode** | ![Camera View](screenshots/camera-detection.png) <!-- ADD: Phone camera + detected pothole --> |
| **SmartFleet Report** | ![Report Success](screenshots/report-success.png) <!-- ADD: Success message + fake GPS + balloons --> |
| **Video Demo** | ![Video Player](screenshots/video-demo.png) <!-- ADD: Video player embedded --> |

---

## 🚀 Overview

**Pothole Patrol AI** is a **real-time computer vision web app** that uses **YOLOv8 (ONNX)** to detect potholes from:
- Uploaded images
- Live phone camera
- Preloaded examples

Built for **fleet managers, city officials, and drivers**, it instantly identifies road hazards and simulates reporting to a **SmartFleet dashboard** for optimized repair routing.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| **📸 Live Camera Detection** | Point your phone at the road — AI highlights potholes instantly |
| **🖼️ Image Upload & Examples** | Upload any photo or try 5 preloaded pothole samples |
| **🎯 Confidence Scoring** | Each pothole tagged with detection confidence |
| **📍 Fake GPS Reporting (Demo)** | Simulates sending location + image to fleet system |
| **🎥 Video Demo** | Watch AI in action on real driving footage |
| **☁️ Cloud-Ready** | Designed for AWS S3 + Lightsail deployment |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|----------|--------|
| **YOLOv8 (ONNX)** | Ultra-fast pothole detection model |
| **ONNX Runtime** | Lightweight inference engine |
| **Streamlit** | Interactive web frontend |
| **OpenCV** | Image preprocessing & bounding box rendering |
| **AWS Lightsail** | Production hosting |
| **AWS S3** | Report storage (future analytics) |
| **Python 3.9+** | Core language |

---

## 🔄 How It Works

```mermaid
graph TD
    A[User opens app] --> B{Choose input}
    B --> C[Upload Photo]
    B --> D[Use Phone Camera]
    B --> E[Select Example]
    C --> F[Preprocess → 640x640]
    D --> F
    E --> F
    F --> G[ONNX Model Inference]
    G --> H[Post-process + NMS]
    H --> I[Draw Blue Boxes + Confidence]
    I --> J{Report?}
    J -->|Yes| K[Fake GPS + Success + Balloons]
    J -->|No| L[View Results]



Input → Image or live camera frame
AI → Runs YOLOv8 ONNX model
Output → Potholes boxed in blue with confidence
Report → Simulates sending to SmartFleet with fake Chicago GPS
Data → Ready for fleet route optimization


🎮 Try the Demo
👉 Live App: https://pothole-patrol-ai.com
👉 Direct Link: http://44.248.45.242:8501
No login. No tracking. No data saved.
Perfect for demos, pitches, or hackathons.

📂 Project Structure
textPothole-Patrol-AI/
│
├── pothole-model.onnx          # YOLOv8 ONNX model
├── app.py                      # Main Streamlit app
├── Example Photos/             # 5 sample images
├── Demo-Videos/                # pothole_demo_h264.mp4
├── screenshots/                # ← ADD YOUR IMAGES HERE
└── README.md                   # ← You're reading it!

🚀 Local Development
Prerequisites

Python 3.9+
pip

Setup
bash# Clone repo
git clone https://github.com/yourusername/Pothole-Patrol-AI.git
cd Pothole-Patrol-AI

# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py
Model (pothole-model.onnx) must be in root directory.

🌍 Deployment (AWS Lightsail)

Launch Ubuntu 22.04 instance
Install Python + Streamlit
Copy files via scp
Run with nohup streamlit run app.py --server.port=8501 &
Open port 8501 in firewall


🛡️ Privacy & Demo Mode
This is a demo.
Photos are not saved
GPS is fake (Chicago neighborhoods)
No user data collected


📄 License
MIT License – Free to use, modify, and deploy.

⭐ Star this project if you like it!
Help us improve road safety — one pothole at a time.




