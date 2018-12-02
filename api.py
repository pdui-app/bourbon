import cv2

import bourbon_


def getVid():
    vidcap = cv2.VideoCapture('eyes.mp4')
    coords = bourbon_.vidToOffsets(vidcap)
    print coords


getVid()
