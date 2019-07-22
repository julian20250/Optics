import poppy
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')

#Constants
lamb=632.8e-9
k=2*np.pi/lamb
d_1 = 45e-2
f=50e-3
a=f/2


coefficients_sequence = [0, 0, 0, 0, 35e-9]
osys = poppy.OpticalSystem()
osys.add_pupil(poppy.CircularAperture(radius=a*100)) #Radius in meters
thinlens = poppy.ZernikeWFE(radius=a*100, coefficients=coefficients_sequence)
osys.add_pupil(thinlens)
osys.add_detector(pixelscale=0.010, fov_arcsec=5.0)
psf = osys.calc_psf(lamb) #Wavelenght in meters
poppy.display_psf(psf, title="", colorbar=False, cmap="gist_gray")

plt.axis('off')
plt.gcf().set_facecolor("black")
a_tmp=f/10
plt.xlim(-2e2*a_tmp, 2e2*a_tmp)
plt.ylim(-2e2*a_tmp, 2e2*a_tmp)
plt.savefig("astigmatism2.png",  bbox_inches='tight', pad_inches = 0)
