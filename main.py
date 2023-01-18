import sys
from dsplot.graph import Graph


def compute_graph(N):
    graph = dict()
    for n in range(1, N + 1):
        graph = add_branch(graph, n)
    return graph


def add_branch(graph, n):
    while n not in graph:
        if n % 2 == 0:
            d = int(n / 2)
        else:
            d = int(3 * n + 1)
        graph[n] = [d]
        n = d
    return graph


def path(graph, n):
    p = graph[n].copy()
    while p[-1] > 1:
        p.append(graph[p[-1]][0])
    return p


def display_graph(graph):
    dsgraph = Graph(graph, directed=True)
    dsgraph.plot(orientation='TB')


def main(N):
    graph = compute_graph(N)
    for k in range(1, N+1):
        p = path(graph, k)
        print(f'{k} ({len(p)}): {path(graph, k)}')
    display_graph(graph)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(20)
