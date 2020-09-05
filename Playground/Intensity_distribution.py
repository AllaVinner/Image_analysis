

def image_floating_to_uint8(inImage):
	"""
		Takes in an 2D numpy array with dtype as a floating and values between 0 - 1
			and transform it into the corresponding image with dtype uint8
	"""

	outImage = inImage.copy()

	# From here we assume that the type is some sort of inexac (decimal and complex) between 0 and 1
	assert np.issubdtype( outImage.dtype, np.floating)
	assert np.all(0.  <=  outImage  )
	assert np.all(        outImage  <= 1.)

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
	assert np.all(0 <= outImage)
	assert np.all(    outImage <= 255)

	outImage = outImage.astype('float32')
	outImage = outImage /255.

	return outImage

def intesity_shifter(inImage):
	imshape = inImage.shape
	outImage = inImage.copy()
	outImage = outImage.flatten()
	for i,p in enumerate(outImage):
		outImage[i] = np.sum(outImage <= p)
	outImage = outImage.reshape(shape = imshape)




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

















