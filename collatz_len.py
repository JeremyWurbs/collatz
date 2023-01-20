import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

from collatz import CollatzGraph

N = 100000
graph = CollatzGraph(N)

x = np.zeros((N+1,))
y = np.zeros((N+1,))
for i in tqdm(range(1, N+1)):
    x[i] = i
    y[i] = graph.len(i)

plt.scatter(x, y, marker='.')
plt.xlabel('n')
plt.ylabel('Sequence Length')
plt.pause(0)
