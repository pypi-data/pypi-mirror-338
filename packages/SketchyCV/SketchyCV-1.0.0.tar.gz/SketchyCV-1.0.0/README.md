# SketchyCV

A simple BGR image to Sketch making tool that need ony the installment of Numpy and OpenCV library.

## Feature:
- Can convert any BGR image to Sketch
- Gives output in MatLike format
- Is lightweight tool

## Installation

You can install it using

```sh
pip install SketchyCV
```

## Usage

### To convert any image to sketch

```py
import cv2
import SketchyCV

image = cv2.imread("filename.jpg")

sketch = SketchyCV.Sketch(image)
```

### To convert live webcam image to sketch

```py
import cv2
import SketchyCV

camera = cv2.VideoCapture(camera_address)

while True:
    ret, frame = cam.read()

    sketch = SketchyCV.Sketch(frame)

    cv2.imshow("window_name", sketch)
    cv2.waitKey(0)

cam.release()
cv2.destroyAllWindows()
```

## Requirements
- Python 3.11+
- OpenCV
- Numpy

## Author
[Rupayan Sarker](https://github.com/rupayan-23)