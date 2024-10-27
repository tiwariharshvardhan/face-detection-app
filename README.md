# Face Detection Application

## Overview

This Face Detection Application uses OpenCV to detect faces in images or in real-time using a webcam. The application allows users to upload an image or activate their webcam, automatically detecting faces and applying a blur effect for privacy.

## Features

- Detects faces in uploaded images.
- Real-time face detection using a webcam.
- Applies a blur effect to detected faces for privacy.
- Simple and user-friendly interface.

## Technologies Used

- Python
- OpenCV
- NumPy

## Installation

### Prerequisites

- Python 3.12.6 installed on your system.
- pip (Python package manager).

### Steps to Install

1. Clone this repository:

   ```bash
   git clone https://github.com/tiwariharshvardhan/face-detection-app.git
   cd face-detection-app

2. Install the required packages:

   ```bash
   pip install opencv-python numpy

### Steps to Run

1. Run the application:

   ```bash
   python face_detection_app.py

2. Choose one of the following options:

   - Detect faces in an image: Enter the path to the image file when prompted.
   - Detect faces using webcam: Press '2' to start the webcam detection. Press 'q' to stop the webcam.
  
### Example

After launching the application, you can see the following options:
```bash
Choose an option:
1. Detect faces in an image
2. Detect faces using webcam
