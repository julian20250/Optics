import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import glob
size=50
filenames = glob.glob("originalImages/*.JPG")
for x in filenames:
    nombre = x[-x[::-1].index("/"):-4]
    # Open Image
    img = Image.open(x).convert("L")
    # Load image into numpy array
    img_data = np.asarray(img)
    lowest = np.nanmin(img_data[np.isfinite(img_data)])
    highest = np.nanmax(img_data[np.isfinite(img_data)])
    # Calculate the original contrast range
    pos_x, pos_y=np.where(img_data == highest)
    new_image=img_data[pos_x[0]-size:pos_x[0]+size, pos_y[0]-size:pos_y[0]+size]


    norm_fourier_img = Image.fromarray(new_image)

    # Save image
    norm_fourier_img.convert("L").save("Cortadas/"+nombre+".JPG")
