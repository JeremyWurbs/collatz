from tqdm import tqdm
from dsplot.graph import Graph


class CollatzGraph(object):
    def __init__(self, N=None, levels=None):
        self.graph = dict()

        if levels is not None:
            self.add_levels(levels)

        if N is None:
            N = 0
        self.N = N

        for n in range(1, self.N+1):
            self.add_branch(n)

    def add_branch(self, n):
        self.N = max((n, self.N))
        while n not in self.graph:
            if n % 2 == 0:
                d = n//2
            else:
                d = 3*n + 1
            self.graph[n] = [d]
            n = d

    def add_levels(self, N):
        for _ in range(N+1):
            self.add_level()

    def add_level(self):
        keys = self.graph.copy().keys()
        if len(keys) == 0:
            self.graph[1] = [4]
            return
        for n in keys:
            self.graph[2*n] = [n]
            if n > 4 and (n-1) % 3 == 0 and ((n-1) // 3) % 2 == 1:
                self.graph[(n-1) // 3] = [n]

    def path(self, n):
        self.add_branch(n)
        p = self.graph[n].copy()
        while p[-1] > 1:
            p.append(self.graph[p[-1]][0])
        return p

    def len(self, n):
        return len(self.path(n))

    def display(self, **kwargs):
        dsgraph = Graph(self.graph, directed=True)
        dsgraph.plot(**kwargs)

    def __call__(self, n):
        return self.path(n)

    def __str__(self):
        str = ''
        for n in range(1, self.N + 1):
            str += f'{n} ({self.len(n)}): {self.path(n)}\n'
        return str
