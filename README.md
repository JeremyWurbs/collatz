# Collatz

# Installation

In order to create png images of the resulting collatz graphs, install graphviz
(used by dsplot):

```commandline
apt install graphviz libgraphviz-dev
```

Then install the package, either through a wheel or just installing the 
dependendies. I.e.

```commandline
git clone https://github.com/JeremyWurbs/collatz.git && cd collatz
```

Followed by one of the following:

```commandline
pip install -r requirements.txt
```

OR

```commandline
python setup.py bdist_wheel
pip install dist/collatz-1.0.0-py3-none-any.whl
```

# Sample

Refer to `main.py` to see how to compute the Collatz graph from 1 to N.

```commandline
python main.py 15
```

The path and path length from 1 to N will be printed to screen, with the final 
graph structure saved to *graph.png*.

![graph.png](resources/graph_N=15.png)

Note: While the `main.py` reference script (and analogous classes below) can 
quickly compute the entire tree for N up to a few tens of millions, the display 
library seems to have difficulty if the number of nodes is above a few 
thousand.

# Collatz Graph 

You may use the CollatzGraph class to compute Collatz paths in your own code, 
play around interactively, or export an entire Collatz graph to a png file.

```python 
from collatz import CollatzGraph

graph = CollatzGraph()
path = graph(10)  # [5, 16, 8, 4, 2, 1]
```

To compute the complete graph for all leaf nodes up to N, pass N in as a 
parameter when instantiating the graph. The graph may then be saved to a png 
with the display method.

```python
from collatz import CollatzGraph

graph = CollatzGraph(N=20)
graph.display(output_path='graph.png')
```

The above code will generate the same image generated by `main.py`. You may 
also generate trees to a given depth using the `levels` parameter when 
instantiating the graph.

```python
from collatz import CollatzGraph

graph = CollatzGraph(levels=21)
graph.display(orientation='TB')
```

![21_levels](resources/21_levels.png)

# Generalized Collatz Graph

If you wish to define the functions applied to even and odd numbers directly,
you may use the GeneralizedCollatz class and pass in user-defined functions, 
resulting in graphs which may or may not always converge back to 1.

```python
from collatz import GeneralizedGraph

graph = GeneralizedGraph(N=20, even_function=lambda n: n // 2, odd_function=lambda n: 3 * n - 1)
graph.display(output_path='3N-1.png')
```

![3N-1](resources/3N-1.png)

As can be seen, unlike the Collatz Conjecture proper (*3N+1*), the *3N-1* case 
has multiple cycles. In general, it is very difficult to prove that a given 
case will *always* go down to one.

```python 
from collatz import GeneralizedGraph

graph = GeneralizedGraph(N=20, even_function=lambda n: n // 2, odd_function=lambda n: 3 * n + 3)
graph.display(output_path='3N+3.png')
```

![3N+3](resources/3N+3.png)

```python 
from collatz import GeneralizedGraph

graph = GeneralizedGraph(N=20, even_function=lambda n: n // 2, odd_function=lambda n: 3 * n - 3)
graph.display(output_path='3N-3.png')
```

![3N+3](resources/3N-3.png)

# Sequence Length

The length of any given set of sequences can also easily be computed. Refer to
(and/or run) `collatz_len.py` to produce the following plot of the sequence 
length for every value of n up to 100,000.

![sequence_length](resources/sequence_length.png)

Feel free to make your own explorations. Utility methods for primality testing 
and prime sieve generation have been given in `utilities.py`, should you want 
to start looking at the intersection of the two. For example, below is a plot 
of the number of primes in each sequence (refer to and/or run `prime_len.py`).

![num_primes](resources/num_primes.png)

# Parallelized Graph Computation

It is also possible to compute the graph with multiple workers, which does 
speed up processing for smaller graphs, but unfortunately is unlikely to 
improve performance for larger graphs as the copying and merging of the 
final results seems to dwarf any performance gains.

```python
import time
from collatz import CollatzGraph, ParallelCollatzGraph

N = 100_000_000

t1 = time.process_time()
CollatzGraph(N=N)
t2 = time.process_time()
print(f'\nSerial computation took {t2-t1:.4f} seconds')

for w in [4, 16]:
    t1 = time.process_time()
    ParallelCollatzGraph(N=N, num_workers=w)
    t2 = time.process_time()
    print(f'Parallel computation with {w} workers took {t2-t1:.2f} seconds')
```

```text
Serial computation took 171.68 seconds
Parallel computation with 4 workers took 423.08 seconds
Parallel computation with 16 workers took 866.08 seconds
```

Note: in addition to taking longer, using 16 workers also takes ~270GB memory.
