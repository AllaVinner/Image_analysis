# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 17:56:37 2020

@author: Computer
"""
import numpy as np


def image_floating_to_uint8(inImage):
    """
        Takes in an 2D numpy array with dtype as a floating and values between 0 - 1
        and transform it into the corresponding image with dtype uint8
    """

    outImage = inImage.copy()

    # From here we assume that the type is some sort of inexac (decimal and complex) between 0 and 1

    assert np.issubdtype( outImage.dtype, np.floating)
    assert np.all(0.  <=  outImage)
    assert np.all(        outImage <= 1.)

    outImage = 255*outImage
    outImage = outImage.astype('uint8')

    return outImage


def image_integer_to_float32(inImage):
    """
        Takes in an 2D numpy array with dtype as a floating and values between 0 - 1
            and transform it into the corresponding image with dtype uint8
    """

    outImage = inImage.copy()

    # From here we assume that the type is some sort of inexac (decimal and complex) between 0 and 1
    assert np.issubdtype( outImage.dtype, np.integer)
    assert np.all(0 <= outImage <= 255)

    outImage = outImage.astype('float32')
    outImage = outImage /255.

    return outImage

def get_gray_image():
    """
        Returns a 4,3 image in gray scale that is sutible for tests.
    """
    img = np.array([[0, 100, 200, 255],
                    [50, 100 , 150, 200],
                    [123, 124,125, 126]])
    return img



def get_intensity_function(img):
    from collections import Counter
    c = Counter(img.flatten())
    
    return np.vectorize(lambda I: c[I])









