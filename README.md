# Collatz

# Installation

In order to create png images of the resulting collatz graphs, install graphviz
(used by dsplot):

```
apt install graphviz libgraphviz-dev
```

Then install the python dependencies:

``` 
pip install -r requirements.txt
```

# Sample

Refer to `main.py` to see how to compute the Collatz graph from 1 to N.

``` 
python main.py 15
```

The path and path length from 1 to N will be printed to screen, with the final 
graph structure saved to *graph.png*.

![graph.png](resources/graph_N=15.png)

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

# Generalized Collatz Graph

If you wish to define the functions applied to even and odd numbers differently,
you may use the GeneralizedCollatz class and pass in the desired functions.

```python
from generalized_collatz import GeneralizedGraph

graph = GeneralizedGraph(N=20, even_function=lambda n: int(n/2), odd_function=lambda n: int(3*n-1))
graph.display(output_path='3N-1.png')
```

![3N-1](resources/3N-1.png)

As can be seen, unlike the Collatz Conjecture proper (*2N+1*), the *2N-1* case 
has multiple cycles. In general, it is very difficult to prove that a given 
case will *always* go down to one.

```python 
from generalized_collatz import GeneralizedGraph

graph = GeneralizedGraph(N=20, even_function=lambda n: int(n/2), odd_function=lambda n: int(3*n+3))
graph.display(output_path='3N+3.png')
```

![3N+3](resources/3N+3.png)

```python 
from generalized_collatz import GeneralizedGraph

graph = GeneralizedGraph(N=20, even_function=lambda n: int(n/2), odd_function=lambda n: int(3*n-3))
graph.display(output_path='3N-3.png')
```

![3N+3](resources/3N-3.png)
