import time

from collatz import CollatzGraph, ParallelCollatzGraph


N = 100

t1 = time.process_time()
graph = CollatzGraph(N=N)
t2 = time.process_time()
print(f'Serial CollatzGraph took {t2-t1} seconds')

t1 = time.process_time()
p_graph4 = ParallelCollatzGraph(N=N, num_workers=4)
t2 = time.process_time()
print(f'Parallel CollatzGraph with 4 workers took {t2-t1} seconds')

t1 = time.process_time()
p_graph16 = ParallelCollatzGraph(N=N, num_workers=16)
t2 = time.process_time()
print(f'Parallel CollatzGraph with 16 workers took {t2-t1} seconds')
