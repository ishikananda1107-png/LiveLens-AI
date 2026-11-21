
import streamlit as st
import cv2
from PIL import Image
from ultralytics import YOLO
from collections import Counter

# Page configuration
st.set_page_config(
    page_title="LiveLens AI",
    page_icon="👁️",
    layout="wide"
)

# Load AI model
@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

# Header
st.title("👁️ LiveLens AI")
st.subheader("AI-Powered Visual Intelligence System")
st.write("Upload an image or capture one using your camera.")

# Sidebar
st.sidebar.title("Settings")
confidence = st.sidebar.slider(
    "Detection Confidence",
    0.10, 1.00, 0.40
)

# Image input
tab1, tab2 = st.tabs(["📁 Upload Image", "📷 Camera"])

with tab1:
    uploaded_file = st.file_uploader(
        "Choose an image",
        type=["jpg", "jpeg", "png"]
    )

with tab2:
    camera_image = st.camera_input("Capture an image")

# Select image
image_file = uploaded_file if uploaded_file else camera_image

if image_file:

    image = Image.open(image_file).convert("RGB")

    st.subheader("Original Image")
    st.image(image, use_container_width=True)

    # Object detection
    with st.spinner("AI is analyzing your image..."):
        results = model.predict(
            image,
            conf=confidence,
            verbose=False
        )

    result = results[0]

    # Draw detection boxes
    annotated = cv2.cvtColor(
        result.plot(),
        cv2.COLOR_BGR2RGB
    )

    st.subheader("AI Detection Results")
    st.image(annotated, use_container_width=True)

    # Detection statistics
    detected_objects = [
        result.names[int(box.cls[0])]
        for box in result.boxes
    ]

    counts = Counter(detected_objects)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Objects Detected", len(detected_objects))

    with col2:
        st.metric("Unique Object Types", len(counts))

    st.subheader("Detection Details")

    if counts:
        for name, count in counts.items():
            st.write(f"✅ {name.title()} — {count}")
    else:
        st.warning("No objects detected. Try another image.")

else:
    st.info("Upload an image or capture one to start AI detection.")
st.divider()
st.caption("LiveLens AI | Python PBL Project")
