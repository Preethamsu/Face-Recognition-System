# 🖼️ Face Recognition System

**Project:** Real-Time Face Recognition Using Python  
**Author:** Preetham Siddapura Umesh  
**Domain:** Computer Vision / Machine Learning / AI  
**Email:** [preetham.umesh2003@gmail.com]

**LinkedIn:** [https://www.linkedin.com/in/preethamsu/]

**Tools & Libraries:** Python, OpenCV, Haar Cascade, NumPy, face_recognition  

---

## 📖 Project Overview

This project implements a **real-time face recognition system** using Python and OpenCV. It can detect faces in images or live video streams and recognize them based on a trained dataset. The system is designed for **security, attendance, or identity verification applications**.  

---

## 🎯 Objectives

1. Detect human faces in images or video streams.  
2. Recognize known faces from a predefined dataset.  
3. Display real-time identification with bounding boxes and labels.  
4. Provide a foundation for security or attendance automation systems.  

---

## 🛠️ Tools & Technologies

- **Python Libraries:**  
  - `OpenCV` – for face detection and image processing  
  - `face_recognition` – for face encoding and recognition  
  - `NumPy` – for numerical operations  
- **Haar Cascade Classifier:** Pre-trained model for detecting faces  
- **Dataset:** Images of known individuals for training the system  

---

## 🔧 Project Structure
Face-Recognition-System/
│
├── data/ # Folder containing training images
├── IP1.py # Image processing / testing scripts
├── start.py # Main script to run the system
├── classifier.xml # Haar Cascade XML classifier
├── haarcascade_frontalface_default.xml
├── name.py # Mapping of recognized names
├── tempCodeRunnerFile.py # Temporary testing code
├── image.jpeg # Sample image for testing
└── README.md # Project documentation

---

## 🖥️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/Preethamsu/Face-Recognition-System.git
Navigate to the project folder:
cd Face-Recognition-System
Install dependencies:
pip install opencv-python face_recognition numpy
Run the main application:
python start.py
The system will open a webcam window and detect/recognize faces in real-time.
📊 Features
✅ Real-time face detection using Haar Cascade
✅ Face recognition with labeled bounding boxes
✅ Works with images or live webcam video
✅ Modular code for easy extension

🔮 Applications
Security & Surveillance Systems
Attendance automation in schools or workplaces
Identity verification for restricted access
AI-powered home automation systems

📌 Next Steps / Improvements:
Integrate with database or CSV for storing attendance logs
Add multiple face recognition support in crowded scenes
Improve recognition accuracy with deep learning models like CNN or FaceNet
Develop a web or mobile interface for monitoring
