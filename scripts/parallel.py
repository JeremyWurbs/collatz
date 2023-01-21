import time

from collatz import CollatzGraph, ParallelCollatzGraph


N = [100, 10000, ]
W = [2, 4, 8, 16, ]

for N_ in N:
    t1 = time.process_time()
    CollatzGraph(N=N_)
    t2 = time.process_time()
    print(f'\nWorkers: 1, Computation Time: \t{t2-t1:.4f} seconds,  \t{N_} Nodes')

    for w in W:
        t1 = time.process_time()
        ParallelCollatzGraph(N=N_, num_workers=w)
        t2 = time.process_time()
        print(f'Workers: {w}, Computation Time: \t{t2-t1:.4f} seconds,  \t{N_} Nodes')
