import numpy as np
from numpy import pi, sin
import matplotlib.pyplot as plt
from scipy.signal import convolve, freqz

import time

x = np.array([1,-2,3,-4,5,0,5,0,5,0,5,0,5,0,5,0,5,0,5],dtype=np.float32)
h = np.ones(4, dtype=np.float32)

Lx = x.size
Lh = h.size
Ly = Lx+Lh-1

y = np.zeros(Ly)

for Ix in range(Lx):
    for Ih in range(Lh):
        y[Ix+Ih] = y[Ix+Ih] + (x[Ix]*h[Ih])

#verification
yy = convolve(x,h,mode='full')

print("[=] x[n] : ",x)
print("[=] h[n] : ",h)
print("[=] Output : ",y)

if np.sum(y-yy)==0:
    print("verified")

#plotting
fig, axs = plt.subplots(3,1)
axs[0].plot(x)
axs[0].set_ylabel('input')

axs[1].stem(h, use_line_collection=True)
axs[1].set_ylabel('system response')

axs[2].plot(y)
axs[2].set_ylabel('output')

plt.show()


