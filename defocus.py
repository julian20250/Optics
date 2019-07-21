# -*- coding: utf-8 -*-
from scipy.special import jv
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
plt.style.use('dark_background')

lamb=632.8e-9
f=50e-3
a=f/10
k=2*np.pi/lamb

r_3=np.linspace(0,a)
phi = np.linspace(0, 2*np.pi)
r_3, phi = np.meshgrid(r_3, phi)
x_grid=r_3*np.cos(phi)
y_grid=r_3*np.sin(phi)
u=.1

int_1=[]
int_2=[]
for ii in r_3:
    m1=[]
    m2=[]
    for jj in ii:
        m1.append(quad(lambda x: x*np.cos(x**4+u*x**2/2)*jv(0,x*jj), 0,1)[0])
        m2.append(quad(lambda x: x*np.sin(x**4+u*x**2/2)*jv(0,x*jj), 0,1)[0])
    int_1.append(m1)
    int_2.append(m2)

int_1, int_2=np.array(int_1), np.array(int_2)
I = np.sqrt(int_1**2+int_2**2)
f=plt.figure(figsize=(12,12))
plt.axis('off')
plt.gcf().set_facecolor("black")

m=plt.pcolormesh(x_grid,y_grid, I, cmap="gist_gray")
m.axes.get_xaxis().set_visible(False)
m.axes.get_yaxis().set_visible(False)
plt.savefig("defocus.png",  bbox_inches='tight', pad_inches = 0)
