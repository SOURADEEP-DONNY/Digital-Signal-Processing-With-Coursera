import numpy as np
import matplotlib.pyplot as plt
from numpy import sin,pi

#parameter settings
A1 = 0.1
F1 = 440
A2 = 0.1
F2 = 4400
Fs = 8000
Td = 10e-3
Ts = 1/Fs
t = np.arange(0,Td,Ts)

#create signal
signal1= A1*sin(2*pi*F1*t)
signal2 = A2*sin(2*pi*F2*t)

#create figure window
fig,axs = plt.subplots(1,2)
axs[0].plot(t, signal1)
axs[0].set_title('Lowpass sampling')

axs[1].plot(t, signal2)
axs[1].set_title('Bandpass sampling')

plt.show()
