# -*- coding: utf-8 -*-
from scipy.special import jv
import matplotlib.pyplot as plt
import numpy as np


plt.style.use('dark_background')
"""
Created on Mon Jul 15 18:09:47 2019

@author: Alejandro
"""


lamb=632.8e-9
f=50e-3
a=f/10
k=2*np.pi/lamb

r_3=np.linspace(0,a)
phi = np.linspace(0, 2*np.pi)
r_3, phi = np.meshgrid(r_3, phi)
x_grid=r_3*np.cos(phi)
y_grid=r_3*np.sin(phi)

I=(k*a*jv(1,k*a)*jv(0, 2*a*r_3/lamb/f)-2*r_3*a*jv(0, k*a)*jv(1,2*a*r_3/lamb/f)/lamb/f)/(k**2-(2*r_3/lamb/f)**2)
f=plt.figure(figsize=(12,12), facecolor="b")
plt.axis('off')
plt.gcf().set_facecolor("black")
m=plt.pcolormesh(x_grid,y_grid, I, cmap="gist_gray")
m.axes.get_xaxis().set_visible(False)
m.axes.get_yaxis().set_visible(False)
plt.savefig("distortion.png",  bbox_inches='tight', pad_inches = 0)
