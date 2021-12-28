import numpy as np
import matplotlib.pyplot as plt
import cv2
import math

img=cv2.imread("D:\pic1.jpg")
mask=5
cv2.imshow("No filter",img)

for i in range(img.shape[0]-mask):
   for j in range(img.shape[1]-mask):
       val = []
       for k in range(mask):
           for l in range(mask):
               if k==l==(math.floor(mask/2)):
                   continue
               else:
                   val.append(img[i+k][j+l])
       img[i+(math.floor(mask/2))][j+(math.floor(mask/2))]=np.median(val)

cv2.imshow("filter",img)
cv2.waitKey(0)
