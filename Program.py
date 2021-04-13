import cv2

def take_snapshot():
    videoCaptureObject=cv2.VideoCapture(0)
    result=true
    while(result)
    ret, frame=videoCaptureObject.read()
    cv2.imwrite("Security Picture.png", image)