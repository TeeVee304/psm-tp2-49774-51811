import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import lfilter

# DADOS DE ENTRADA
fonte = [4, 4]
ouvinte = [0, 0]

dist = np.sqrt((ouvinte[0] - fonte[0])**2 + (ouvinte[1] - fonte[1])**2)
print('dist:', dist)
ang = np.acos((ouvinte[0] - fonte[0]) / dist)
# ang = np.degrees(ang)
ang = ang*100 / np.pi
print('ang:', ang)

fs, sound = wavfile.read('./sounds/mosquito.wav')
filename = f'./HRTF/elev0/H0e{ang:03.0f}a.wav'
fs, HRTF = wavfile.read(filename)

plt.figure()
plt.plot(sound)
plt.show()

yLBinaural = np.convolve(sound, HRTF[:, 0])
yRBinaural = np.convolve(sound, HRTF[:, 1])
yBinaural = np.vstack((yLBinaural, yRBinaural)).T

wavfile.write('./sounds/out/binaural.wav', fs, yBinaural.astype(np.int16))