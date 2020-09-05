# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 19:06:39 2020

@author: Computer
"""





"""
    Handle continues images and conversion to discrete once
    Assignment 1, task 1
"""


import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import matplotlib.pyplot as plt
import IA_library as IA

img = lambda x,y: x*(1-y) + y*(1-x)


delta = 0.01
X,Y = np.mgrid[0:1+delta/2:delta, 0:1+delta/2:delta]

I = img(X,Y)

# Resize I
q = 50
J = (I*q).astype('uint8')
J = np.where(J == q, q-1, J )

fig, axe = plt.subplots(2)
axe[0].imshow(I, cmap = 'binary')
axe[1].imshow(J, cmap = 'binary')

If = IA.get_intensity_function(I)
Jf = IA.get_intensity_function(J)

"""
count = Counter(I.flatten())
p_r = lambda v: count[v]


plt.hist(I.flatten(), 15,(0,15))

"""







