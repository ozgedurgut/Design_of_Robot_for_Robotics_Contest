from typing import List

import cv2
import numpy as np

img = cv2.imread('mapping.png', cv2.IMREAD_UNCHANGED )

print('Original Dimensions : ', img.shape)

width = 350
height = 350
dim = (width, height)

# resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)



hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)

lower_range = np.array([84, 98, 0])
upper_range = np.array([179, 255, 255])

mask = cv2.inRange(hsv, lower_range, upper_range)

cv2.imshow('image', resized)
cv2.imshow('mask', mask)

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
	a: List[int] = [0]*6
	i = 0

	for c in contours:
		M = cv2.moments(c)
		cX = int(M["m10"] / M["m00"])
		cY = int(M["m01"] / M["m00"])
		a[i] = cX
		a[i+1] = cY
		cv2.drawContours(resized, [box], 0, (0, 255, 255), 2)
		cv2.circle(resized, (cX, cY), 5, (255, 0, 255), -1)
		#cv2.putText(resized, s, (cX - 20, cY - 20),
		#cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
		i = i + 2
		print(a)


	cv2.imshow("Original Tespit", resized)


cv2.waitKey(0)
cv2.destroyAllWindows