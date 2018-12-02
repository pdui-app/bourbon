import cv2

from eyeDetect import getOffset, detect, getLeftAndRightEyes, containsPoint

haarFaceCascade = cv2.CascadeClassifier(
    "./optimeyes/haarcascades/haarcascade_frontalface_alt.xml")
haarEyeCascade = cv2.CascadeClassifier(
    "./optimeyes/haarcascades/haarcascade_eye.xml")
