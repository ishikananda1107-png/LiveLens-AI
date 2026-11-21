<div align="center">

# 👁️ LiveLens AI

**AI-powered real-world object detection in your browser**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-111F68)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv&logoColor=white)

</div>

---

## 📌 About

LiveLens AI is a visual intelligence web app. Upload an image or capture one with your camera, and a YOLOv8 model identifies everyday objects, draws labelled bounding boxes, and reports how many of each it found.

Built as a Python project-based learning (PBL) project.

## ✨ Features

- 📁 **Upload an image** (JPG, JPEG, PNG) or 📷 **capture a photo** with your camera
- 🎯 **Object detection** with YOLOv8, pretrained on the COCO dataset
- 🟦 **Labelled bounding boxes** drawn on the detected objects
- 🎚️ **Adjustable confidence** from the sidebar slider
- 📊 **Detection summary**: total objects, unique object types, and a count for each

## 🛠️ Tech Stack

| Area | Tools |
|------|-------|
| Language | Python |
| Web app | Streamlit |
| Detection model | Ultralytics YOLOv8 |
| Image processing | OpenCV, Pillow, NumPy |

## ⚙️ How It Works

1. The user uploads an image or captures one with the camera.
2. The image is passed to the YOLOv8 model at the chosen confidence level.
3. Detected objects are drawn on the image with labels.
4. The app shows the annotated result along with object counts.

## 🚀 Run Locally

```bash
git clone https://github.com/ishikananda1107-png/LiveLens-AI.git
cd LiveLens-AI
pip install -r requirements.txt
streamlit run app.py
```

> The YOLOv8 model file (`yolov8n.pt`) downloads automatically on the first run.

## 📁 Project Structure

```
LiveLens-AI/
├── app.py              # Streamlit app
├── requirements.txt    # Dependencies
└── README.md
```

## 👩‍💻 Author

**Ishika Nanda**, B.Tech Computer Science Engineering (AI/ML)

[GitHub](https://github.com/ishikananda1107-png) · [LinkedIn](https://www.linkedin.com/in/ishika-nanda-3b6941376/)
