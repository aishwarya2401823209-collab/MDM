import numpy as np
import matplotlib.pyplot as plt

N = 10000
bits = np.random.randint(0, 2, N)
s = 2*bits - 1
snr = range(11)
ber = []

for db in snr:
    noise = np.random.randn(N)/np.sqrt(2*10**(db/10))
    r = s + noise
    ber.append(np.mean((r > 0) != bits))

plt.semilogy(snr, np.array(ber)+1e-5, "o-")
plt.xlabel("SNR (dB)")
plt.ylabel("BER")
plt.title("Noise Analysis")
plt.grid()
plt.show()