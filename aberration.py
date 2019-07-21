# Ref: https://www.youtube.com/watch?v=gJ2m0dd7QpU
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import glob

filenames = glob.glob("*.png")
file = open("Resultados/intensidadMaximaAberraciones.txt", "w")
for x in filenames:
    nombre = x[:-4]
    print(nombre)
    # Open Image
    img = Image.open(x).convert("L")
    # Load image into numpy array
    img_data = np.asarray(img)**(1/2.)
    # Perform the 2-D fast fourier transform on the image data
    fourier = np.fft.fft2(img_data)
    # Move the zero-frequency component to the center of the fourier spectrum
    fourier = np.fft.fftshift(fourier)
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
    step=1
    l=[]
    count = 0
    rango = range(step, width, 2*step)
    for ii in rango:
        l.append(sum(sum(norm_fourier[:, ii-step:ii+step])))
        count+=1
    l = np.array(l)
    maximum = l.max()
    file.write("%s %f\n"%(x,maximum))
    l = l/maximum
    f=plt.figure(figsize=(12,12))
    plt.plot(rango,l)
    plt.xlabel("Posición")
    plt.ylabel("Intensidad")
    plt.savefig("Resultados/Intensity/"+x)
    #Section of Picture
    # Convert the normalized data into an image
    norm_fourier_img = Image.fromarray(norm_fourier)

    # Save image
    norm_fourier_img.convert("L").save("Resultados/"+nombre+".JPG")
file.close()
