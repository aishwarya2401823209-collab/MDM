import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
d = np.linspace(0, 5, 500)
signal = np.zeros(len(d), dtype=complex)

for i in range(10):
    p = np.random.rand() * 6.28
    signal += np.exp(1j * (p + 20*d*np.random.rand()))

rssi = 20*np.log10(np.abs(signal)/np.mean(np.abs(signal)))

plt.plot(d, rssi)
plt.xlabel("Distance")
plt.ylabel("Signal Level (dB)")
plt.title("Multipath Fading")
plt.grid()
plt.show()