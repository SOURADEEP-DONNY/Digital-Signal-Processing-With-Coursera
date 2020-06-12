import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, pi

# parameter settings
A1 = 0.1
F1 = 440
A2 = 0.05
F2 = 1220
Fs = 8000
Td = 10e-3
Ts = 1 / Fs
t = np.arange(0, Td, Ts)

# create signal
signal1 = A1 * sin(2 * pi * F1 * t)
signal2 = A2 * sin(2 * pi * F2 * t)

# addition
add = signal1 + signal2

# subtraction
sub = signal1 - signal2

# multiplication
mul = signal1 * signal2

# division
eps = 10e-9
div = signal1 / (signal2 + eps)

# create figure window
fig, axs = plt.subplots(3, 2)
axs[0, 0].plot(t, signal1)
axs[0, 0].set_title('signal1')

axs[0, 1].plot(t, signal2)
axs[0, 1].set_title('signal2')

axs[1, 0].plot(t, add)
axs[1, 0].set_ylabel('addition')

axs[1, 1].plot(t, sub)
axs[1, 1].set_ylabel('subtraction')

axs[2, 0].plot(t, mul)
axs[2, 0].set_ylabel('multiplication')

axs[2, 1].plot(t, div)
axs[2, 1].set_ylabel('division')

plt.show()
