"""
	A function that takes in an image (or file) and a color vector, and a sesnsitivity and
		returns (saves) an image with 'only' that color. 



"""
# Imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image 
from math import exp, sqrt
import colorsys
import IA_library as IA

def splash(domain ,color, sesnsitivity):
    """
        domain - original image
        color_vec - np array (RGB) describing the desired color
        sensitivity - float which is about how close the the desired color is okay
    """
    hsv_color = np.array(colorsys.rgb_to_hls(*color))

    rows, cols, depth = domain.shape
    # Create new (empty) image
    image = np.zeros(shape = domain.shape)


    # Go through the image array
    for row in range(rows):
        for col in range(cols):
            # for each pixel calculate the distance between the pixel's color and the desiered one.
            pixel = domain[row, col,:]

            hsv_pixel = np.array(colorsys.rgb_to_hls(*pixel))
            hsv_delta = hsv_color-hsv_pixel

            dist = sqrt( hsv_delta[0]**2+hsv_delta[2]**2)


            # Get the multiplication factor? (normal disrtibution)
            #factor = exp(-(dist/(sqrt(2)*sensitivity)**2))
            factor = max(-(dist**4)/sensitivity+1, 0)
        

            # Assign that value to the new image
            hsv_pixel[2] = factor*hsv_pixel[2]
            rgb = np.array(colorsys.hls_to_rgb(*hsv_pixel))

            image[row, col, :] = rgb
    return image


fname = 'mar.jpg'
color = np.array(
        [250,150,150])
sensitivity = 2

# Read file
domain = mpimg.imread(fname)
domain = domain/255



fig, (ax1,ax2) = plt.subplots(1,2)
ax1.imshow(domain)

image = splash(domain, color, sensitivity)

ax2.imshow(image)
plt.show()





