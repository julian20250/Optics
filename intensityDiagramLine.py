import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import glob

filenames = glob.glob("originalImages/*.JPG")
for x in filenames:
    nombre = x[-x[::-1].index("/"):-4]
    #nombre = x[:-4]
    print(nombre)

    # Open Image
    img = Image.open(x).convert("L")
    # Load image into numpy array
    img_data = np.asarray(img)**(1/2.)

    maximum = np.max(img_data)
    i,j = np.unravel_index(img_data.argmax(), img_data.shape)
    height, width = img_data.shape
    I = img_data[i, :]
    I = I/maximum
    X = range(width)

    f=plt.figure(figsize=(12,12))
    plt.plot(X, I)
    plt.savefig("Resultados/IntensidadLine/"+nombre+".png")
