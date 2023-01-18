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

Run `main.py` to see compute the Collatz graph from 1 to N.

``` 
python main.py 20
```

The path and path length from 1 to N will print to screen, with the final graph
structure saved to *graph.png*.

[graph.png](resources/graph.png)

