import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageFilter

# Read an image
img = Image.open('grey.jpg')
plt.imshow(img)
plt.show()

img = np.asarray(img)
# Apply log transformation method
high = np.max(img)
print("high value : ", high)
low = np.min(img)
print("low Value : ", low)
print(type(img))
##print(np.shape(img))
##size = np.shape(img)
print(img.shape[0])
for i in range(0, img.shape[0] - 1):
    for j in range(0, img.shape[1] - 1):
        # Get pixel value at (x,y) position of the image
        pixelColorVals = img[i,j];
        # Invert color
        redPixel    = (pixelColorVals[0] - low) / (high - low); # Negate red pixel
        greenPixel  = (pixelColorVals[1] - low) / (high - low); # Negate green pixel
        bluePixel   = (pixelColorVals[2] - low) / (high - low); # Negate blue pixel
                                   
        # Modify the image with the inverted pixel values
        img[i,j,0] = redPixel;
        img[i,j,1] = greenPixel;
        img[i,j,2] = bluePixel;

# Specify the data type so that
# float value will be converted to int
img = np.array(img, dtype = np.uint8)

# Display both images

plt.imshow(img)
plt.show()
