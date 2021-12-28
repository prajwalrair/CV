import numpy as np
import matplotlib.pyplot as plt
import cv2
import math
# Read the image in greyscale
rows, cols = (100, 100)
arr = [[0 for i in range(cols)] for j in range(rows)]
arr=np.array(arr)
for i in range(100):
   n=0
   for j in range(50):
       arr[i][j]=n
       n=n+10
   for k in range(41,61):
       arr[i][k]=255
   arr[50][80]=255
   arr[50][85]=150
   arr[50][90]=20
   arr[50][95]=240




print(type(arr))
print(arr)
plt.imshow(arr,cmap="gray")
plt.show()
cv2.waitKey(0)
