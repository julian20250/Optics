import poppy
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from scipy.optimize import minimize
import time
import warnings

#Constants
lamb=632.8e-9
k=2*np.pi/lamb
d_1 = 45e-2
f=50e-3
a=f/2

def aberration(astigmatism, spherical, distortion, defocus):
    coefficients_sequence = [0, distortion, 0, defocus, astigmatism,0,0,0,0,0,0, spherical]
    osys = poppy.OpticalSystem()
    osys.add_pupil(poppy.CircularAperture(radius=a*100)) #Radius in meters
    thinlens = poppy.ZernikeWFE(radius=a*100, coefficients=coefficients_sequence)
    osys.add_pupil(thinlens)
    osys.add_detector(pixelscale=0.010, fov_arcsec=5.0)
    psf = osys.calc_psf(lamb) #Wavelenght in meters
    with plt.style.context('dark_background'):
        poppy.display_psf(psf, title="", colorbar=False, cmap="gist_gray")

        plt.axis('off')
        plt.gcf().set_facecolor("black")
        a_tmp=f/10
        plt.xlim(-2e2*a_tmp, 2e2*a_tmp)
        plt.ylim(-2e2*a_tmp, 2e2*a_tmp)
        plt.savefig("tmp.png",  bbox_inches='tight', pad_inches = 0)
    plt.clf()

    # Open Image
    img = Image.open("tmp.png").convert("L")
    # Load image into numpy array
    img_data = np.asarray(img)

    maximum = np.max(img_data)
    i,j = np.unravel_index(img_data.argmax(), img_data.shape)
    height, width = img_data.shape
    I = img_data[i, :]
    I = I[I!=0]
    I = I/maximum
    return I

def shapeSim(simul):
    X = np.linspace(0, 100, len(simul))
    Y = range(100)
    L=[]
    for x in Y:
        m=list(abs(X-x))
        L.append(m.index(min(m)))
    return L

def compFun(simul, real):
    return sum((simul[shapeSim(simul)]-real))**2

def minFunc(abb, realData):
    I=aberration(abb[0], abb[1], abb[2], abb[3])
    return compFun(I, realData)
nombre = "DSC_0030"
x ="ResultadosInversos/"+nombre+".JPG"
nombre = x[-x[::-1].index("/"):-4]
#nombre = x[:-4]
print(nombre)

# Open Image
img = Image.open(x).convert("L")
# Load image into numpy array
img_data = np.asarray(img)

maximum = np.max(img_data)
i,j = np.unravel_index(img_data.argmax(), img_data.shape)
height, width = img_data.shape
I = img_data[i, :]
I = I/maximum
X = range(len(I))
# 35e-9,35e-9,35e-9,35e-9
# init stopper
ast, sphe, dist, defo =3.621792960819685e-09,-5.98521944889911e-09,5.217368544739121e-09,2.426643878714564e-09

textstr = 'astigmatism ='+"{:.2e}".format(ast)+"\n"+"spherical ="+"{:.2e}".format(sphe)+"\n"+"distortion ="+"{:.2e}".format(dist)+"\n"+"defocus ="+"{:.2e}".format(defo)
ab=aberration(ast,sphe,dist,defo)
#plt.style.use('seaborn-bright')
#plt.gcf().set_facecolor("white")
fig, ax = plt.subplots()
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
plt.plot(X, I, label="Diagrama Real")
plt.plot(np.linspace(0,100,len(ab)), ab, label="Diagrama Simulado")
plt.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
    verticalalignment='top', bbox=props)
plt.xlabel("Píxeles")
plt.ylabel("Intensidad")
plt.legend()
plt.tight_layout()
plt.savefig("comparison/"+nombre+".png")
plt.clf()
