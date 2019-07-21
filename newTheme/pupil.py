from scipy.special import jv
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import dblquad
lamb=632.8e-9
k=2*np.pi/lamb
d_1 = 45e-2
f=50e-3
a=f/10

length= 50
x_array = np.linspace(-10, 10, length)
y_array = np.linspace(-10, 10, length)

x_array, y_array = np.meshgrid(x_array, y_array)
I_real = np.zeros(x_array.shape)
I_img = np.zeros(x_array.shape)

height, width = x_array.shape
count=0

for x in range(height):
    for y in range(width):
        I_real[x][y] = dblquad(lambda r,theta: r*np.cos(x_array[x][y]*r*np.cos(theta)*k/d_1), -a, a, lambda ii: 0, lambda ii: 2*np.pi)[0]
        I_img[x][y] = dblquad(lambda r,theta: r*np.sin(y_array[x][y]*r*np.cos(theta)*k/d_1), -a, a, lambda ii: 0, lambda ii:2*np.pi)[0]
        count+=1
        print("%i/%i"%(count, width*height), end="\r")
I= (I_real**2+I_img**2)**.5
f=plt.figure(figsize=(12,12))
plt.axis('off')
plt.gcf().set_facecolor("black")

m=plt.pcolormesh(x_array,y_array, I, cmap="gist_gray")
m.axes.get_xaxis().set_visible(False)
m.axes.get_yaxis().set_visible(False)
plt.savefig("pupil2.png",  bbox_inches='tight', pad_inches = 0)
