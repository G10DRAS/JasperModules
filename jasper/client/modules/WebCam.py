# -*- coding: utf-8-*-

# Copyright 2016 g10dras.
__author__ = 'g10dras'

import cv2
import sys
import re
from datetime import datetime
from client import jasperpath
from os.path import expanduser

WORDS = ["HACK", "CAM", "WEBCAM", "PHOTO"]

def handle(text, mic, profile):

	home = expanduser("~")
	WINDOW_NAME = "Face Detective"

	cascPath = jasperpath.data('cascade', 'haarcascade_frontalface_default.xml')
	faceCascade = cv2.CascadeClassifier(cascPath)

	video_capture = cv2.VideoCapture(0)
	cv2.namedWindow(WINDOW_NAME, cv2.CV_WINDOW_AUTOSIZE)

	while True:
		# Capture frame-by-frame
		ret, frame = video_capture.read()

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.3,
			minNeighbors=5,
			minSize=(30, 30),
			flags=cv2.cv.CV_HAAR_SCALE_IMAGE
		)

		print "Number Of Faces Detected {0}!".format(len(faces))
		
		# Draw a rectangle around the faces
		for (x, y, w, h) in faces:
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

		# Display the resulting frame
		cv2.startWindowThread()
		cv2.imshow(WINDOW_NAME, frame)

		k = cv2.waitKey(1)
		if k == 27:         # wait for ESC key to exit
			break
		elif len(faces) > 0: # faces greter than 0 save image
			photoname = home + "/out/%s.png" % datetime.now().strftime("%Y%m%d-%H%M%S")	
			print photoname
			cv2.imwrite( photoname, frame)
			break			

	# When everything is done, release the capture
	video_capture.release()
	cv2.waitKey(1)
	cv2.destroyAllWindows()
	cv2.waitKey(1)
	mic.say("Face detected")

def isValid(text):
    """
        Returns True if the input is related to Webcam.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return any(word in text.upper() for word in WORDS)
	
