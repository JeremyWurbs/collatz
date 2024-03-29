import sys
from collatz import CollatzGraph, GeneralizedGraph


def main(N):
    graph = CollatzGraph(N=N)
    print("2N+1 (Collatz Conjecture)")
    print(graph)
    graph.display(output_path='3N+1.png', orientation='TB')

    graph = GeneralizedGraph(N=N, even_function=lambda n: n//2, odd_function=lambda n: 3*n-1)
    print("\n2N-1")
    print(graph)
    graph.display(output_path='3N-1.png', orientation='TB')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(20)
