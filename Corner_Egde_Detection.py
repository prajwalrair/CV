from skimage.io import imread 
from skimage.color import rgb2gray 
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt

img = imread('grey.jpg')
imggray = rgb2gray(img)
from scipy import signal as sig
import numpy as np
def gradient_x(imggray): 
  kernel_x = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
  return sig.convolve2d(imggray, kernel_x, mode='same')
def gradient_y(imggray): 
  kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]]) 
  return sig.convolve2d(imggray, kernel_y, mode='same') 
I_x = gradient_x(imggray) 
I_y = gradient_y(imggray)
Ixx = gaussian_filter(I_x**2, sigma=1) 
Ixy = gaussian_filter(I_y*I_x, sigma=1)
Iyy = gaussian_filter(I_y**2, sigma=1)
k = 0.05 # determinant 
detA = Ixx * Iyy - Ixy ** 2 
# trace traceA = Ixx + Iyy harris_response = detA - k * traceA ** 2
k = 0.05
# determinant
detA = Ixx * Iyy - Ixy ** 2
# trace
traceA = Ixx + Iyy
    
harris_response = detA - k * traceA ** 2

# height, width = imggray.shape
# harris_response = []
# window_size = 6
# offset = int(window_size/2)
# for y in range(offset, height-offset):
#     for x in range(offset, width-offset):
#         Sxx = np.sum(Ixx[y-offset:y+1+offset, x-offset:x+1+offset])
#         Syy = np.sum(Iyy[y-offset:y+1+offset, x-offset:x+1+offset])
#         Sxy = np.sum(Ixy[y-offset:y+1+offset, x-offset:x+1+offset])
        
#         #Find determinant and trace, use to get corner response
#         det = (Sxx * Syy) - (Sxy**2)
#         trace = Sxx + Syy
#         r = det - k*(trace**2)
        
#         harris_response.append(r)
img_copy_for_corners = np.copy(img)
img_copy_for_edges = np.copy(img)

for rowindex, response in enumerate(harris_response):
    for colindex, r in enumerate(response):
        if r > 0:
            # this is a corner
            img_copy_for_corners[rowindex, colindex] = [255,0,0]
        elif r < 0:
            # this is an edge
            img_copy_for_edges[rowindex, colindex] = [0,255,0]
    
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10,10))
ax[0].set_title("corners found")
ax[0].imshow(img_copy_for_corners)
ax[1].set_title("edges found")
ax[1].imshow(img_copy_for_edges)
plt.show()
