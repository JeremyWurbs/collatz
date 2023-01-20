from dsplot.graph import Graph
from collatz import CollatzGraph


class GeneralizedGraph(CollatzGraph):
    def __init__(self, N=None, even_function=lambda n: n//2, odd_function=lambda n: 3*n + 1):
        super().__init__(N=0)
        self.even_function = even_function
        self.odd_function = odd_function

        if N is None:
            N = 0
        self.N = N

        for n in range(1, self.N+1):
            self.add_branch(n)

    def add_branch(self, n):
        self.N = max((n, self.N))
        while n not in self.graph:
            if n % 2 == 0:
                d = self.even_function(n)
            else:
                d = self.odd_function(n)
            self.graph[n] = [d]
            n = d
        return self.graph

    def path(self, n):
        self.add_branch(n)
        p = self.graph[n].copy()
        while p[-1] > 1 and self.graph[p[-1]][0] not in p:
            p.append(self.graph[p[-1]][0])
        return p
