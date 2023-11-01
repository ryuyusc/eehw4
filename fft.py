import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

# Number of samplepoints
N = 600
# sample spacing
T = 1.0 / 200.0
x = np.linspace(0.0, N * T, N)

y = np.loadtxt('digital_signal.txt')

yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)

fig, ax = plt.subplots()

#Uncomment this section to plot the signal itself
# ax.plot(x,y)
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')

#uncomment this section to plot the fourier transform output using the FFT algorithm
ax.plot(xf, 2.0 / N * np.abs(yf[:N // 2]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.show()

