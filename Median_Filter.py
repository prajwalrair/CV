import numpy as np
import matplotlib.pyplot as plt
import cv2
import math
# Read the image in greyscale
#img = [[1,255,0],[100,50,200],[0,0,255]]
img=cv2.imread("grey.png",0)
mask=3
cv2.imshow("No filter",img)
# Iterate over each pixel and change pixel value to binary using np.binary_repr() and store it in a list.
##for i in range(img.shape[0]):
##   for j in range(img.shape[1]):
##       #print(img[i][j], end=" ")

print(math.floor(mask/2))
print(img.shape)
print("-------------------------------")
for i in range(500):
   for j in range(500):
       val = []
       img[i,j] = img[i+1,j] + img[i-1,j] + img[j+1,i] + img[j-1,i] - (4* img[i,j])
##       for k in range(mask):
##           for l in range(mask):
##               if k==l==(math.floor(mask/2)):
##                   continue
##               else:
##                   val.append(img[i+k][j+l])
##
##
##       img[i+(math.floor(mask/2))][j+(math.floor(mask/2))]=np.median(val)# np.min/np.max/np.median
##       #print(img[i][j], end=" ")

   #print()
cv2.imshow("filter",img)
cv2.waitKey(0)
