import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

# Intensity
I=np.array([16928551.35,16390380.35,15949680.04,15346706.71,15826632.56,16150200.77,15476417.74,16725929.38,16729221.38,16411080.89,15967303.28,16036915.94,16361193.05,15607785.78,15357027.71,15698285.9,16224203.27,16435064.99,16529801.08,15773304.93,17298044.67,17293719.01,16587849.05])
a=np.array([22,20,18,16,16,14,13,11,10,9,8,7.1,6.3,5.6,5,4.5,4,3.5,2.8,2.5,2.2,2,1.8])

order = np.argsort(a)
a, I= a[order], I[order] 

xnew = np.linspace(a[0], a[-1],400)
power_smooth = spline(a,I,xnew)
f=plt.figure(figsize=(12,12))
plt.scatter(a,I)
plt.plot(xnew, power_smooth)
plt.show()