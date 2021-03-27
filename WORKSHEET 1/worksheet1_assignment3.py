import numpy as np
import matplotlib.pyplot as plt
from numpy import sin,pi
import sounddevice as sd

#parameter settings
A1 = 1
F1 = 1000
A2 = 1
F2 = 7000
Fs = 8000
Td = 30e-3
Ts = 1/Fs
t = np.arange(0,Td,Ts)

#create signal
signal1= A1*sin(2*pi*F1*t)
signal2 = A2*sin(2*pi*F2*t)

signal3 = signal1 + signal2

#create figure window
fig,axs = plt.subplots(1,1)
axs.plot(t, signal3)

sd.play(signal3)
plt.show()
