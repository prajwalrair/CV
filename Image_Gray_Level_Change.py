#----- Example Python program for negative transformation of a Digital Image -----
 
# import Pillow modules
from PIL import Image
from PIL import ImageFilter
import math
 
# Load the image
img = Image.open("log_image.png")
 
# Display the original image
img.show()
 
# Read pixels and apply negative transformation
for i in range(0, img.size[0]-1):
    for j in range(0, img.size[1]-1):
        # Get pixel value at (x,y) position of the image
        pixelColorVals = img.getpixel((i,j));
        # Invert color
        redPixel    = int(math.log(1 + pixelColorVals[0]));# Negate red pixel
        greenPixel  = int(math.log(1 + pixelColorVals[1])); # Negate green pixel
        bluePixel   = int(math.log(1+ pixelColorVals[2])); # Negate blue pixel
                   
        # Modify the image with the inverted pixel values
        img.putpixel((i,j),(redPixel, greenPixel, bluePixel));
 
# Display the negative image
img.show();
