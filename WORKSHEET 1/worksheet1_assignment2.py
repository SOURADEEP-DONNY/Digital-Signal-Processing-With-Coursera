import numpy as np
import matplotlib.pyplot as plt
from numpy import sin,pi
import sounddevice as sd

#parameter settings
A = 1
F = 7000
Fs = 8000
Td = 10e-3
Ts = 1/Fs
t = np.arange(0,Td,Ts)

#create signal
signal = A*sin(2*pi*F*t)

#create figure window
fig,axs = plt.subplots(1,1)
axs.plot(t, signal)

sd.play(signal)
plt.show()
