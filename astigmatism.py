# -*- coding: utf-8 -*-
from scipy.special import jv
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
plt.style.use('dark_background')
"""
Created on Mon Jul 15 18:09:47 2019

@author: Alejandro
"""

lamb=632.8e-9
f=50e-3
a=f/10

r_3=np.linspace(0,a/10e1)
phi = np.linspace(0, 2*np.pi)
r_3, phi = np.meshgrid(r_3, phi)
x_grid=r_3*np.cos(phi)
y_grid=r_3*np.sin(phi)
int_1=[]
int_2=[]
for ii in r_3:
    m1=[]
    m2=[]
    for jj in ii:
        m1.append(quad(lambda x: x*np.cos(np.pi*x**2/lamb)*jv(0,np.pi*x**2/lamb)*jv(0, 2*x*jj/lamb/f), a/10,a)[0])
        m2.append(quad(lambda x: x*np.sin(np.pi*x**2/lamb)*jv(0,np.pi*x**2/lamb)*jv(0, 2*x*jj/lamb/f), a/10,a)[0])
    int_1.append(m1)
    int_2.append(m2)

int_1, int_2=np.array(int_1), np.array(int_2)
I = np.sqrt(int_1**2+int_2**2)
f=plt.figure(figsize=(12,12))
plt.axis('off')
plt.gcf().set_facecolor("black")
m= plt.pcolormesh(x_grid, y_grid, I, cmap="gist_gray")
m.axes.get_xaxis().set_visible(False)
m.axes.get_yaxis().set_visible(False)
plt.savefig("astigmatism.png",  bbox_inches='tight', pad_inches = 0)
