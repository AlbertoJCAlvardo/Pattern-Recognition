# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:06:46 2022

@author: argen
"""

import cv2
img = cv2.imread('llaves1.jpeg',2)

ret, bw_img = cv2.threshold(img,100,255,cv2.THRESH_BINARY)

black = []

for i in range(len(bw_img)):
    for j in range(len(bw_img[0])):
        black.append([i,j])


cv2.imshow("Binary Image",bw_img)

cv2.waitKey(0)
cv2.destroyAllWindows()