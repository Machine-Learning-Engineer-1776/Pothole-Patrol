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
- **Phone camera** — Snap a photo of the road and detect instantly  
- **Video demo** — Watch AI analyze real driving footage  

Built for **fleet managers, city officials, and drivers**, it instantly identifies road hazards and simulates reporting to a **SmartFleet dashboard** for optimized repair routing.

---

## Key Features

### 1. Preloaded Examples  
Try 5 sample images instantly — see AI detect potholes with zero setup.

<img width="1445" height="145" alt="{EDFB24E1-3A5F-4058-B769-3024535AC8E7}" src="https://github.com/user-attachments/assets/23cc516c-f5c2-45e1-aabd-b8c83471b7dc" />

<img width="288" height="228" alt="{F455DF30-DFC9-4293-B6F9-C3338310AB90}" src="https://github.com/user-attachments/assets/b923565e-f16a-41ed-ae08-502c34f932b1" />


---

### 2. Upload Your Own Photo  
Drag and drop any road image — AI analyzes and highlights potholes immediately.

<img width="1429" height="401" alt="{06DD5DF1-5901-4065-BAD8-7BA2A4790AB2}" src="https://github.com/user-attachments/assets/1f925e3a-ebd5-4f21-8c84-a971e6ad158f" />

---

### 3. Camera Detection  
Take a photo with your phone or webcam (Streamlit `camera_input`) and the model detects potholes in the snapshot.

<img width="197" height="29" alt="{AE42037B-C6FD-45A6-BB9F-EE562A01C055}" src="https://github.com/user-attachments/assets/e35d11cf-5df5-44a1-82e9-bba0ae499286" />
 
---

### 4. Report to SmartFleet (Demo)  
Tap **Report To SmartFleet**: a demo step that shows a randomly chosen (fake) Chicago location. Nothing is actually sent.

<img width="1261" height="625" alt="{1BAF322B-C392-48D4-AA59-4571BB459383}" src="https://github.com/user-attachments/assets/38bbe220-7a20-4267-b167-076d844143ec" />

---

### 5. Video Demo  
Play a pre-recorded driving clip with pothole detections.

<img width="258" height="178" alt="{50032FB5-278D-4F5E-BCAD-C2979F98EAB3}" src="https://github.com/user-attachments/assets/37396ba1-1c08-438f-8cb0-99f1758e786b" />

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| **YOLOv8 (ONNX)** | Pothole detection model (640×640 input, confidence threshold 0.4, NMS) |
| **ONNX Runtime** | Lightweight inference engine |
| **Streamlit** | Interactive web frontend |
| **OpenCV** | Image preprocessing & bounding box rendering |
| **AWS Lightsail** | Production hosting |
| **Python 3.9+** | Core language |

## Model and results

- Detector: YOLOv8 exported to ONNX (`Model/pothole-model.onnx`; the PyTorch weights are `Model/pothole-model.pt`)
- Inference runs on CPU with ONNX Runtime; boxes above 0.4 confidence are kept after non-max suppression
- Training data and evaluation metrics (e.g. mAP) are **not included in this repo yet**, so no accuracy figures are claimed here. The demo video and sample detections show the model's behaviour qualitatively.

---

## How It Works

```mermaid
graph TD
    A[Pothole Patrol AI] --> B{Select Mode}
    B --> C[Preloaded Examples]
    B --> D[Upload Image]
    B --> E[Live Camera]
    B --> F[Video Demo]
    C --> G[AI Detection]
    D --> G
    E --> G
    F --> H[Play Video]
    G --> I[Blue Boxes + Confidence]
    I --> J{Report?}
    J -->|Yes| K[Fake GPS + Balloons]
    J -->|No| L[Done]
    K --> M[SmartFleet Dashboard]
```

---
## Try the Demo

**Live App (mobile camera works):** [https://pothole-patrol-ai.com](https://pothole-patrol-ai.com)

> **No login. No tracking. No data saved.**  

---

## Project Structure

```
app.py                      # Streamlit app (ONNX inference, upload / camera / examples / video)
requirements.txt
Model/pothole-model.onnx    # YOLOv8 model exported to ONNX (used by the app)
Model/pothole-model.pt      # YOLOv8 PyTorch weights
Demo Video/pothole_demo.mp4 # demo driving clip
README.md
```

## Run Locally

```bash
pip install -r requirements.txt onnxruntime
cp Model/pothole-model.onnx .          # app.py loads pothole-model.onnx from the working directory
streamlit run app.py
```

Notes: the app looks for sample images in an `Example Photos/` folder (pothole1.jpg … pothole5.jpg) and the video at `Demo-Videos/pothole_demo_h264.mp4`; those paths aren't in this repo yet, so the examples and video sections show a "not found" message until you add them. `onnxruntime` is imported by `app.py` but not yet listed in `requirements.txt`.

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
