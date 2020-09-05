

"""
	Idea:

	give me an image and a kernel it returns the altered image

"""
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
from PIL import Image


#def filter(original, kernel):
w = np.array([0.1,0.5,1.0])
b = np.array([1.0,0.5,0.1])

original = np.array( [ [ w,w,w,b,b],
					   [ w,w,w,b,b],
					   [ w,w,b,b,w],
					   [ w,w,b,b,b],
					   [ b,w,b,b,b]])

fname = 'mar.jpg'
# Read file
domain = mpimg.imread(fname)
domain = domain/255
original = domain

kernel_size = 51
kernel = 1/(kernel_size**2)*np.ones(shape = (kernel_size, kernel_size,3))
#original = np.array( [ [ [0.7,0.2,0.4],[0.1,0.1,0.7]], [ [0.0,0.9,0.1],[0.0,1.0,0.5]]])

fig, axs = plt.subplots(1,2)
axs[0].imshow(original)

# get sizes
im_rows, im_cols, im_channels = original.shape
ker_rows, ker_cols, ker_channels = kernel.shape 

ker_width = int((ker_rows-1)/2)

new_image = np.zeros(shape = original.shape)

# Add padding
original_padded = np.zeros(shape = (im_rows+2*ker_width, im_cols+2*ker_width, im_channels))
original_padded[ker_width:-ker_width, ker_width:-ker_width, :] = original

# sweep over the image

for row in range(ker_width, im_rows+ker_width):
	for col in range(ker_width, im_cols+ker_width):
		mat = original_padded[row-ker_width: row+ker_width+1,
							  col-ker_width: col+ker_width+1,
							  :]
		mat = mat*kernel
		new_value = mat.sum(axis = (0,1))
		new_image[row-ker_width, col-ker_width,:] = new_value


## cut out the matrix

## Multiply

## Add

## Assign to knew.

axs[1].imshow(new_image)
plt.show()



















