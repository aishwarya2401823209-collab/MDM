import matplotlib.pyplot as plt

bands = ["MF", "VHF", "UHF", "SHF", "EHF"]
freq = [1, 100, 1000, 10000, 100000]

plt.bar(bands, freq)
plt.yscale("log")
plt.xlabel("Bands")
plt.ylabel("Frequency")
plt.title("EM Spectrum")
plt.show()