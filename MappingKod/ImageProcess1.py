from typing import List

import cv2
import numpy as np
import imutils

def color_seg(choice):
    if choice == 'blue':
        lower_hue = np.array([100,30,30])
        upper_hue = np.array([150,148,255])
    elif choice == 'white':
        lower_hue = np.array([0,0,0])
        upper_hue = np.array([0,0,255])
    elif choice == 'black':
        lower_hue = np.array([0,0,0])
        upper_hue = np.array([50,50,100])
    return lower_hue, upper_hue


# Take each frame
frame = cv2.imread('mapping.png')

#frame = cv2.imread('images/road_1.jpg')

frame = cv2.resize(frame, (350, 350))

#frame = imutils.resize(frame, height = 350)
#frame = imutils.resize(frame, width=350)
chosen_color = 'black'


# Convert BGR to HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# define range of a color in HSV
lower_hue, upper_hue = color_seg(chosen_color)


# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_hue, upper_hue)


cv2.imshow('frame',frame)
cv2.imshow('mask',mask)
(contours,_) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
center = None
if len(contours) > 0:

	c = max(contours, key = cv2.contourArea)

	rect = cv2.minAreaRect(c)

	((x,y), (width,height), rotation) = rect


	s = "x: {}, y: {}, width: {}, height:{}, rotation:{}".format(np.round(x), np.round(y), np.round(width), np.round(height), np.round(rotation))
	print(s)

	box = cv2.boxPoints(rect)
	box = np. int64(box)

	#a = np.array([], np.int16)
	b: List[int] = [0]*6
	j = 0

	for c in contours:
		M = cv2.moments(c)
		cX = int(M["m10"] / M["m00"])
		cY = int(M["m01"] / M["m00"])
		b[j] = cX
		b[j+1] = cY
		cv2.drawContours(frame, [box], 0, (0, 255, 255), 2)
		cv2.circle(frame, (cX, cY), 5, (255, 0, 255), -1)
		#cv2.putText(resized, s, (cX - 20, cY - 20),
		#cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
		j = j + 2
		print(b)
		print(mask)


	cv2.imshow("Original Tespit", frame)


cv2.waitKey(0)