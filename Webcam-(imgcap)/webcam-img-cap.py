import cv2
import time

imgcapture = cv2.VideoCapture(0)
result = True

while result:
    ret, frame = imgcapture.read()
    name = int(round(time.time() * 1000))
    name = f'E:/Python-Programs/PythonProjects/WebCam/Images-Captured/{name}.jpg'
    cv2.imwrite(name, frame)
    result = False
    print("Image Captured.. ")

imgcapture.release()
