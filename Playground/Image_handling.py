
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('JandJ.jpg')


fig, axs = plt.subplots(2,2)

imgplot = axs[0,0].imshow(img)

s_img = img[:,:,0]
s_imgplot = axs[0,1].imshow(s_img)
s_imgplot.set_cmap('hot')

nb_img = img.copy()
nb_img[:,:,0] = 0
nb_img[:,:,1] = 0
nb_imgplot = axs[1,0].imshow(nb_img)


plt.show()










































