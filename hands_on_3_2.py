import time
import numpy as np
import matplotlib.pyplot as plt


def f(n):
    x = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            x += 1
    return x


n_values = np.arange(1, 201, 10)  
times = []

for n in n_values:
    start_time = time.time()
    f(n)
    end_time = time.time()
    times.append(end_time - start_time)


coefficients = np.polyfit(n_values, times, 2)
polynomial = np.poly1d(coefficients)


plt.figure(figsize=(10, 6))
plt.scatter(n_values, times, color="blue", label="Measured Times")
plt.plot(n_values, polynomial(n_values), color="red", label=f"Fitted Polynomial: {coefficients[0]:.3e}*n^2 + {coefficients[1]:.3e}*n + {coefficients[2]:.3e}")
plt.xlabel("n")
plt.ylabel("Execution Time (seconds)")
plt.title("Execution Time vs n for Function f(n)")
plt.legend()
plt.grid(True)
plt.show()