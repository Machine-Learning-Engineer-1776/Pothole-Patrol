Pothole Patrol AI
Real-time pothole detection for safer roads and smarter fleet management.

AI-powered detection in action — potholes highlighted in real-time.

Overview
Pothole Patrol AI is a custom computer vision application that uses YOLOv8 to detect potholes in real-time from images and live camera feeds. Built with Streamlit and deployed on AWS Lightsail, it empowers drivers, fleet managers, and city officials to identify road hazards instantly — improving safety and optimizing repair routes.

Key Features

































FeatureDescriptionReal-Time DetectionUse your phone camera to detect potholes liveImage UploadUpload any road photo — AI highlights potholes with confidence scoresPreloaded Examples5 sample images for instant demoVideo DemoWatch AI detect potholes in a driving clipSmartFleet ReportingLog detections with GPS for route optimizationCloud IntegrationReports saved to AWS S3 for fleet analytics

Tech Stack





































TechnologyPurposeYOLOv8 (ONNX)High-speed pothole detectionStreamlitInteractive web appOpenCVImage processingONNX RuntimeEfficient model inferenceAWS LightsailHostingAWS S3Report storageGeocoderGPS capture

How It Works

Upload a photo or use live camera
AI model runs inference on every frame
Potholes are boxed in real-time
Report captures image + GPS → saved to S3
Data feeds SmartFleet for route optimization


Demo
Try it now:
https://pothole-patrol-ai.com

Works on iPhone & Android — use camera for live detection.


Installation & Setup (For Developers)
bash# Clone repo
git clone https://github.com/yourusername/pothole-patrol-ai.git
cd pothole-patrol-ai

# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py

Model Details

Model: pothole-model.onnx (YOLOv8 custom-trained)
Input: 640x640 RGB
Classes: pothole
Confidence Threshold: 0.4
NMS IoU: 0.45


Future Roadmap

























FeatureStatusLive Video RecordingPlannedSmartFleet API IntegrationPlannedHeatmap DashboardPlannedOffline ModePlanned

Contributing
We welcome contributions!

Open an issue
Submit a pull request
Improve the model


License
All rights reserved. For commercial use or licensing, contact the author.


Pothole Patrol AI — Because every road deserves to be safe.


Built with ❤️ by Ron Lance
GitHub: github.com/yourusername/pothole-patrol-ai
Live App: https://pothole-patrol-ai.com
