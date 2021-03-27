import numpy as np
from numpy import pi,sin
import matplotlib.pyplot as plt
from scipy.signal import convolve, freqz
import time
import soundfile as sf
from playsound import playsound

Fs = 16000

fig, axs = plt.subplots(3,1)

speech, Fs = sf.read('./cleanspeech.wav')
speech = speech/np.max(np.abs(speech))
axs[0].plot(speech)
axs[0].set_ylabel('Speech')

imp, Fs = sf.read('./hallway_imp.wav')
axs[1].plot(imp)
axs[1].set_ylabel('Filter \n Impulse')

output=convolve(speech,imp,mode='same')
output=output/np.max(np.abs(output))

axs[2].plot(output)
axs[2].set_ylabel('output')
sf.write('./filter_speech.wav',output, Fs)

playsound('./cleanspeech.wav')
time.sleep(2)
playsound('./filter_speech.wav')

plt.show()

                             
