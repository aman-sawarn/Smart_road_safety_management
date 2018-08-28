import numpy as np
import cv2
from copy import deepcopy
from PIL import Image
import pytesseract as tess
import os
def preprocess(img):
	# cv2.imshow("Input",img)
	imgBlurred = cv2.GaussianBlur(img, (5,5), 0)
	gray = cv2.cvtColor(imgBlurred, cv2.COLOR_BGR2GRAY)

	sobelx = cv2.Sobel(gray,cv2.CV_8U,1,0,ksize=3)
	cv2.imshow("Sobel",sobelx)
	cv2.waitKey(0)
	ret2,threshold_img = cv2.threshold(sobelx,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	cv2.imshow("Threshold",threshold_img)
	cv2.waitKey(0)
	return threshold_img
