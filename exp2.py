import matplotlib.pyplot as plt
import numpy as np

i, j = 2, 1
N = i*i + i*j + j*j
Q = np.sqrt(3*N)

for x in range(5):
    for y in range(5):
        plt.scatter(x, y, s=700)
        plt.text(x, y, f"F{(x+y)%N+1}",
                 ha="center", va="center")

plt.title(f"Frequency Reuse N={N}, Q={Q:.2f}")
plt.show()

print("Cluster size:", N)
print("Reuse ratio:", round(Q, 2))