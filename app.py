import streamlit as st
import cv2
import numpy as np
import onnxruntime as ort
import boto3
import geocoder
import os
import random

# === PAGE CONFIG ===
st.set_page_config(page_title="Pothole Patrol", page_icon="🚧")  # FIXED: Real emoji

# === S3 (KEEPING FOR NOW — NOT USED IN REPORT) ===
s3 = boto3.client(
    's3',
    aws_access_key_id="AKIAWPEXTJOZPQARVOZQ",
    aws_secret_access_key="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"
)
S3_BUCKET = "porthole-patrol-smartfleet"

# === LOAD ONNX MODEL ===
@st.cache_resource
def load_model():
    return ort.InferenceSession("pothole-model.onnx")

session = load_model()

# === PREPROCESS ===
def preprocess(img):
    img = cv2.resize(img, (640, 640))
    img = img.astype(np.float32) / 255.0
    img = np.transpose(img, (2, 0, 1))
    img = np.expand_dims(img, axis=0)
    return img

# === POSTPROCESS ===
def postprocess(outputs, orig_img, conf_threshold=0.4, iou_threshold=0.45):
    boxes = []
    output = outputs[0][0].T
    bboxes = output[:, :4]
    class_scores = output[:, 4:]
    confidences = class_scores.max(axis=1)
    class_ids = class_scores.argmax(axis=1)

    h, w = orig_img.shape[:2]
    for i, conf in enumerate(confidences):
        if conf > conf_threshold and class_ids[i] == 0:
            cx, cy, bw, bh = bboxes[i]
            x1 = int((cx - bw / 2) * w / 640)
            y1 = int((cy - bh / 2) * h / 640)
            x2 = int((cx + bw / 2) * w / 640)
            y2 = int((cy + bh / 2) * h / 640)
            if x1 < x2 and y1 < y2:
                boxes.append([x1, y1, x2, y2, float(conf)])

    if len(boxes) > 0:
        boxes = np.array(boxes)
        x1, y1, x2, y2, scores = boxes[:, 0], boxes[:, 1], boxes[:, 2], boxes[:, 3], boxes[:, 4]
        indices = cv2.dnn.NMSBoxes(
            [[int(x1), int(y1), int(x2 - x1), int(y2 - y1)] for x1, y1, x2, y2 in zip(x1, y1, x2, y2)],
            scores.tolist(),
            conf_threshold,
            iou_threshold
        )
        if len(indices) > 0:
            boxes = boxes[indices.flatten()].tolist()
        else:
            boxes = []

    return boxes

# === FAKE CHICAGO GPS LOCATIONS (DEMO ONLY) ===
FAKE_LOCATIONS = [
    (41.8781, -87.6298, "Chicago Loop"),
    (41.9000, -87.6500, "Wrigleyville"),
    (41.8500, -87.6500, "Pilsen"),
    (41.9200, -87.7000, "Logan Square"),
    (41.8800, -87.7000, "Ukrainian Village"),
    (41.9483, -87.6555, "Lincoln Park"),
    (41.7900, -87.6000, "Hyde Park"),
]

# === UI ===
st.title("🚧 Pothole Patrol")  # FIXED
st.markdown("**AI-powered pothole detection for safer roads and smarter fleets**")

# === HOW IT WORKS ===
st.markdown("""
<div style='text-align: center; padding: 1rem 0;'>
    <h3 style='color: #2E86AB;'>🎯 How It Works</h3>
    <p style='color: #666; font-size: 1em;'>Discover the core features of Pothole Patrol below:</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**🖼️ Detect Potholes from Images**")  # FIXED
    st.markdown("Choose a preloaded example or upload your own photo — AI instantly highlights all potholes.")

with col2:
    st.markdown("**📸 Take a Photo & Report**")  # FIXED
    st.markdown("**Take a photo** of any road — AI detects potholes. Tap **Report To SmartFleet** to simulate sending.")

with col3:
    st.markdown("**🎥 Play Video Demo**")  # FIXED
    st.markdown("See Pothole Patrol in action with a real-world driving demo.")

st.markdown("<hr style='border: 2px solid #2E86AB;'>", unsafe_allow_html=True)

# === DETECT FROM IMAGES SECTION ===
st.markdown("### 🖼️ Detect Potholes from Images")  # FIXED

# === EXAMPLE PHOTOS ===
st.markdown("#### Try a Preloaded Example")
st.markdown("**What You're Seeing**: Select a sample image to see AI pothole detection in action. Results appear instantly with highlighted potholes.")
EXAMPLE_DIR = "Example Photos"

example_images = {
    "Pothole 1": "pothole1.jpg",
    "Pothole 2": "pothole2.jpg",
    "Pothole 3": "pothole3.jpg",
    "Pothole 4": "pothole4.jpg",
    "Pothole 5": "pothole5.jpg"
}

if os.path.exists(EXAMPLE_DIR):
    example_options = ["Select an example..."] + list(example_images.keys())
    selected_example = st.selectbox(
        "Choose a sample image:",
        options=example_options,
        index=0,
        help="Pick from 5 preloaded pothole examples"
    )
else:
    st.warning("Example Photos folder not found.")
    selected_example = "Select an example..."

# === UPLOAD PHOTO ===
st.markdown("#### Upload Your Own Photo")
st.markdown("**What You're Seeing**: Upload any road photo — AI detects and highlights potholes with confidence scores.")
uploaded_file = st.file_uploader("Choose image...", type=["jpg", "jpeg", "png"])

# === PROCESS IMAGE (EXAMPLE OR UPLOAD) ===
img = None
source = None

if selected_example != "Select an example...":
    example_path = os.path.join(EXAMPLE_DIR, example_images[selected_example])
    if os.path.exists(example_path):
        img = cv2.imread(example_path)
        source = "example"
    else:
        st.error(f"Example image not found: {example_path}")

elif uploaded_file:
    img = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)
    source = "upload"

if img is not None:
    orig_img = img.copy()
    
    input_tensor = preprocess(orig_img)
    outputs = session.run(None, {"images": input_tensor})
    boxes = postprocess(outputs, orig_img, conf_threshold=0.4)
    
    st.write(f"**{len(boxes)} pothole(s) detected**")
    
    for box in boxes:
        x1, y1, x2, y2, conf = box
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        cv2.rectangle(orig_img, (x1, y1), (x2, y2), (255, 0, 0), 3)
        label = f"pothole {conf:.2f}"
        (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
        cv2.rectangle(orig_img, (x1, y1 - 25), (x1 + w, y1), (255, 0, 0), -1)
        cv2.putText(orig_img, label, (x1, y1 - 5), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
    st.image(cv2.cvtColor(orig_img, cv2.COLOR_BGR2RGB), caption="Potholes Detected")

# === CAMERA ===
st.markdown("<hr style='border: 2px solid #2E86AB;'>", unsafe_allow_html=True)
st.markdown("### 📸 Take a Photo & Report")  # FIXED
st.markdown("**What You're Seeing**: Take a snapshot of the road. The AI analyzes the image and highlights any detected potholes. Tap **Report To SmartFleet** to simulate a submission with fake GPS coordinates (for demo only).")

if st.button("Open Phone Camera"):
    st.session_state.camera_active = True

if st.session_state.get("camera_active", False):
    camera_image = st.camera_input("Point camera at road...", key="live")
    
    if camera_image:
        img = cv2.imdecode(np.frombuffer(camera_image.getvalue(), np.uint8), 1)
        orig_img = img.copy()
        
        input_tensor = preprocess(orig_img)
        outputs = session.run(None, {"images": input_tensor})
        boxes = postprocess(outputs, orig_img, conf_threshold=0.4)
        
        st.write(f"**{len(boxes)} pothole(s) detected**")
        
        for box in boxes:
            x1, y1, x2, y2, conf = box
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cv2.rectangle(orig_img, (x1, y1), (x2, y2), (255, 0, 0), 3)
            label = f"pothole {conf:.2f}"
            (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
            cv2.rectangle(orig_img, (x1, y1 - 25), (x1 + w, y1), (255, 0, 0), -1)
            cv2.putText(orig_img, label, (x1, y1 - 5), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        st.image(cv2.cvtColor(orig_img, cv2.COLOR_BGR2RGB), caption="Potholes Detected")
        
        if st.button("Report To SmartFleet"):
            fake_lat, fake_lon, fake_area = random.choice(FAKE_LOCATIONS)
            
            st.success("**Thank You!**")
            st.markdown(f"""
            **We are recording your GPS coordinates:**  
            **{fake_lat}, {fake_lon}**  
            _({fake_area}, Chicago)_

            This pothole report will be added to the **SmartFleet Pothole Database** for route optimization.

            <div style="text-align: center; margin: 20px 0;">
                <p style="font-size: 3em; margin: 0;">🚛</p>
                <p style="margin: 8px 0 0;"><strong>Reported to SmartFleet</strong><br>
                <a href="http://35.89.230.31:8501/" target="_blank" style="color: #2E86AB; text-decoration: none; font-weight: bold;">35.89.230.31:8501</a></p>
            </div>

            <hr style="border: 1px dashed #ccc; margin: 20px 0;">
            <p style="font-size: 0.9em; color: #7f8c8d;">
            <strong>Demo Mode:</strong> This is a <strong>simulation</strong>.<br>
            • Your photo is <strong>not saved</strong><br>
            • These GPS coordinates are <strong>fake</strong><br>
            • Your real location is <strong>not tracked</strong>
            </p>
            """, unsafe_allow_html=True)
            
            st.balloons()
    
    if st.button("Stop Camera"):
        st.session_state.camera_active = False
        st.experimental_rerun()

# === VIDEO DEMO BUTTON (BOTTOM) ===
st.markdown("<hr style='border: 2px solid #2E86AB;'>", unsafe_allow_html=True)
st.markdown("### 🎥 Play Video Demo")  # FIXED
st.markdown("**What You're Seeing**: Watch a pre-recorded demo of Pothole Patrol in action — see how the AI detects potholes in real time while driving. (This is a video, not live processing.)")

if st.button("Play Video Demo"):
    video_path = "Demo-Videos/pothole_demo_h264.mp4"
    if os.path.exists(video_path):
        st.video(video_path)
    else:
        st.error("Video not found. Run ffmpeg conversion.")