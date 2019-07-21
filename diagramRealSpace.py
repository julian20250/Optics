import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

import glob

filenames = glob.glob("*.png")
for x in filenames:
    nombre = x[:-4]
    img = Image.open(x).convert("L")

    img_data = np.asarray(img)**(1/2.)
    limit = 3
    height, width = img_data.shape
    for x in range(height):
        for y in range(width):
            if img_data[x][y] < limit:
                img_data[x][y]=0
    step=1
    l=[]
    count = 0
    rango = range(step, width, 2*step)
    noiseStep=3
    rango2 = rango[::noiseStep]
    for ii in rango:
        l.append(sum(sum(img_data[:, ii-step:ii+step])))
        count+=1
    l = np.array(l)
    L = np.array([sum(l[x:x+noiseStep-1])/noiseStep for x in range(0,len(l),noiseStep)])
    maximum = l.max()
    maximum2= L.max()
    l = l/maximum
    L = L/maximum2
    f=plt.figure(figsize=(12,12))
    plt.plot(rango,l)
    #plt.plot(rango2, L)
    plt.xlabel("Posición")
    plt.ylabel("Intensidad")
    plt.savefig("Resultados/IntesidadRealAberraciones/"+nombre+".png")
    print(nombre)
