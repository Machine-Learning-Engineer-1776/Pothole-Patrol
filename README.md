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

- **Preloaded examples** — Try 5 built-in pothole samples  
- **Upload your own image** — Drag and drop any road photo  
- **Live phone camera** — Point and detect in real time  
- **Video demo** — Watch AI analyze real driving footage  

Built for **fleet managers, city officials, and drivers**, it instantly identifies road hazards and simulates reporting to a **SmartFleet dashboard** for optimized repair routing.

---

## Key Features (In App Order)

### 1. Preloaded Examples  
Try 5 sample images instantly — see AI detect potholes with zero setup.

![Preloaded Examples](screenshots/upload-detection.png)  
*Sample image with blue bounding boxes and confidence scores.*

---

### 2. Upload Your Own Photo  
Drag and drop any road image — AI analyzes and highlights potholes immediately.

![Upload Detection](screenshots/upload-detection.png)  
*Uploaded image with detected potholes and confidence labels.*

---

### 3. Live Camera Detection  
Open your phone camera — point at the road — AI detects potholes **in real time**.

![Live Camera Detection](screenshots/camera-detection.png)  
*Live phone view with instant pothole detection.*

---

### 4. Report to SmartFleet (Demo)  
Tap **Report To SmartFleet** — simulates sending image + fake GPS to fleet system.

![Report Success](screenshots/report-success.png)  
*Success screen with fake Chicago GPS, balloons, and SmartFleet link.*

---

### 5. Video Demo  
Watch a pre-recorded driving clip — see AI detect potholes frame by frame.

![Video Demo](screenshots/video-demo.png)  
*Video player paused on a frame with active pothole detection.*

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

## Try the Demo

**Live App (mobile camera works):** [https://pothole-patrol-ai.com](https://pothole-patrol-ai.com)

> **No login. No tracking. No data saved.**  
> Perfect for demos, pitches, or hackathons.

---

## Project Structure

**Root Directory:**
- `pothole-model.onnx` → YOLOv8 ONNX model
- `app.py` → Main Streamlit app
- `Example Photos/` → 5 sample images
- `Demo-Videos/` → pothole_demo_h264.mp4
- `screenshots/` → ← ADD YOUR IMAGES HERE
- `README.md` → ← You’re reading it!

---

## Deployment (AWS Lightsail)

1. Launch **Ubuntu 22.04** instance  
2. Install Python + Streamlit  
3. Copy files via `scp`  
4. Run: `nohup streamlit run app.py --server.port=8501 &`  
5. Open port `8501` in firewall  

---

## Privacy & Demo Mode

> **This is a demo.**  
> - Photos are **not saved**  
> - GPS is **fake** (Chicago neighborhoods)  
> - No user data collected  

---

**Made with love for smarter cities**
