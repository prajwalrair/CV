import matplotlib.pyplot as plt
import cv2
# Read the image in greyscale
img = cv2.imread('grey.jpg',0)
print(type(img))
plt.hist(img,256)
plt.show()
