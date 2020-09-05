
from IA_library import image_floating_to_uint8  as f2i
from IA_library import image_integer_to_float32 as i2f

import IA_library as IA


def intesity_shifter(inImage):
    imshape = inImage.shape
    outImage = inImage.copy()
    outImage = outImage.flatten()
    for i,p in enumerate(outImage):
        outImage[i] = np.sum(outImage <= p)
    outImage = outImage.reshape(shape = imshape)



def get_small_gray_image():
    """
        Returns a 4,3 image in gray scale that is sutible for tests.
    """
    img = np.zeros([[0, 100, 200, 255],
                    [50, 100 , 150, 200],
                    [123, 124,125, 126]])
    return img



#def gray_transformation(image, f):
"""
    Take in an image o

"""

import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 
from PIL import Image

img = mpimg.imread('dark_pic.jpg')


"""
histogram of an image

"""

# Mean over colors
gray = img.mean(axis = 2)
vals = img.mean(axis = 2).flatten()
plt.hist(vals,255)
plt.xlim([0,255])
plt.show()

















