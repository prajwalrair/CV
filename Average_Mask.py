import numpy as np
import matplotlib.pyplot as plt
import cv2
# Read the image in greyscale
img = cv2.imread("grey.jpg",0)
#plt.hist(img,256)
#plt.show()
mask=3
cv2.imshow("No filter",img)
# Iterate over each pixel and change pixel value to binary using np.binary_repr() and store it in a list.
for i in range(3):
   for j in range(3):
       print(img[i][j], end=" ")
val=[]

print("-------------------------------")
for i in range(img.shape[0]-mask):
   for j in range(img.shape[1]-mask):
       sum=0
       for k in range(mask):
           for l in range(mask):
               if k==l:
                   continue
               else:
                   sum=sum+img[i+k][j+l]
       avg=sum/((mask*mask)-1)
       img[i+1][j+1]=avg
       #print(img[i][j], end=" ")

   #print()
cv2.imshow("filter",img)
#plt.hist(img,256)
#plt.show()
cv2.waitKey(0)
print(val)
