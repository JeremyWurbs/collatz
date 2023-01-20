import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

from collatz import CollatzGraph
from utils import is_prime


N = 10000
graph = CollatzGraph(N)

x = np.zeros((N+1,))
y = np.zeros((N+1,))
for n in tqdm(range(1, N+1)):
    x[n] = n
    y[n] = sum([1 if is_prime(x) else 0 for x in graph(n)])

plt.scatter(x, y, marker='.')
plt.title('Number of Primes per Sequence')
plt.xlabel('n')
plt.ylabel('Number of Primes')
plt.pause(0)
