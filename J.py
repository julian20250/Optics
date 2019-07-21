# -*- coding: utf-8 -*-
from scipy.special import jv
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('dark_background')
"""
Created on Mon Jul 15 17:02:11 2019

@author: Alejandro
"""
v=np.linspace(0,10)
phi = np.linspace(0, 2*np.pi)
v, phi = np.meshgrid(v, phi)
x_grid=v*np.cos(phi)
y_grid=v*np.sin(phi)
y= abs(np.exp(-1j*v**2/4)*(2*jv(1,v)/v))
f=plt.figure(figsize=(12,12))
plt.axis('off')
plt.gcf().set_facecolor("black")
m=plt.pcolormesh(x_grid,y_grid, y, cmap="gist_gray")
m.axes.get_xaxis().set_visible(False)
m.axes.get_yaxis().set_visible(False)
plt.savefig("abs.png",  bbox_inches='tight', pad_inches = 0)
