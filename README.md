# **Pothole Patrol AI**  
**Real-time pothole detection for safer roads and smarter fleet management.**

*AI-powered detection in action — potholes highlighted in real-time.*

http://44.248.45.242:8501/
---

## **Overview**

**Pothole Patrol AI** is a custom **computer vision application** that uses **YOLOv8** to detect potholes in real-time from images and live camera feeds. Built with **Streamlit** and deployed on **AWS Lightsail**, it empowers drivers, fleet managers, and city officials to identify road hazards instantly — improving safety and optimizing repair routes.

---

## **Key Features**

| Feature | Description |
|--------|-------------|
| **Real-Time Detection** | Use your phone camera to detect potholes live |
| **Image Upload** | Upload any road photo — AI highlights potholes with confidence scores |
| **Preloaded Examples** | 5 sample images for instant demo |
| **Video Demo** | Watch AI detect potholes in a driving clip |
| **SmartFleet Reporting** | Log detections with GPS for route optimization |
| **Cloud Integration** | Reports saved to **AWS S3** for fleet analytics |

---

## **Tech Stack**

| Technology | Purpose |
|----------|--------|
| **YOLOv8 (ONNX)** | High-speed pothole detection |
| **Streamlit** | Interactive web app |
| **OpenCV** | Image processing |
| **ONNX Runtime** | Efficient model inference |
| **AWS Lightsail** | Hosting |
| **AWS S3** | Report storage |
| **Geocoder** | GPS capture |

---

## **How It Works**

1. **Upload** a photo or use **live camera**  
2. **AI model** runs inference on every frame  
3. **Potholes** are boxed in **real-time**  
4. **Report** captures image + GPS → saved to **S3**  
5. **Data feeds SmartFleet** for route optimization

---

## **Demo**

**Try it now:**  
[https://pothole-patrol-ai.com](https://pothole-patrol-ai.com)
http://44.248.45.242:8501/

> *Works on **iPhone & Android** — use camera for live detection.*

---

## **Installation & Setup (For Developers)**

```bash
# Clone repo
git clone https://github.com/yourusername/pothole-patrol-ai.git
cd pothole-patrol-ai

# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py
