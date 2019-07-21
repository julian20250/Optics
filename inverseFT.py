# Ref: https://www.youtube.com/watch?v=gJ2m0dd7QpU
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import glob

filenames = glob.glob("Cortadas/*.JPG")
file = open("ResultadosInversos/intensidadMaxima.txt", "w")
for x in filenames:
    nombre = x[-x[::-1].index("/"):-4]
    print(nombre)
    # Open Image
    img = Image.open(x).convert("L")
    # Load image into numpy array
    img_data = np.asarray(img)**(1/2.)
    # Perform the 2-D fast fourier transform on the image data
    fourier = np.fft.ifft2(img_data)
    # Move the zero-frequency component to the center of the fourier spectrum
    fourier = np.fft.ifftshift(fourier)
    # Compute the magnitudes (absolute magnitude) of the complex numbers
    fourier = abs(fourier)
    # Compute the common logarithm of each value to reduce the dynamic range
    #fourier = np.log10(fourier)
    # Find the minimum and maximum
    lowest = np.nanmin(fourier[np.isfinite(fourier)])
    highest = np.nanmax(fourier[np.isfinite(fourier)])
    # Calculate the original contrast range
    original_range = highest-lowest
    # Normalize the fourier image data ("stretch" the contrast)
    norm_fourier = (fourier - lowest)/original_range*255

    #Section of intensity diagram
    height, width = norm_fourier.shape
    step=20
    l=[]
    count = 0
    rango = range(step, width, 2*step)
    noiseStep=3
    rango2 = rango[::noiseStep]
    for ii in rango:
        l.append(sum(sum(norm_fourier[:, ii-step:ii+step])))
        count+=1
    l = np.array(l)
    L = np.array([sum(l[x:x+noiseStep-1])/noiseStep for x in range(0,len(l),noiseStep)])
    maximum = l.max()
    maximum2= L.max()
    file.write("%s %f\n"%(nombre,maximum))
    l = l/maximum
    L = L/maximum2
    f=plt.figure(figsize=(12,12))
    plt.plot(rango,l)
    plt.plot(rango2, L)
    plt.xlabel("Posición")
    plt.ylabel("Intensidad")
    plt.savefig("Resultados/Intensity/"+nombre+".png")
    #Section of Picture
    # Convert the normalized data into an image
    norm_fourier_img = Image.fromarray(norm_fourier)

    # Save image
    norm_fourier_img.convert("L").save("ResultadosInversos/"+nombre+".JPG")
    plt.cla()
file.close()
