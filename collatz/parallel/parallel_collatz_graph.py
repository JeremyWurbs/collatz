from multiprocessing import Queue
from collections import ChainMap

from collatz import CollatzGraph, CollatzWorker, chunk


class ParallelCollatzGraph(CollatzGraph):
    def __init__(self, N=None, levels=None, num_workers=1):
        super().__init__(levels=levels)

        if N is None:
            N = 0
        self.N = N

        if N is not None:
            workers = list()
            chunks = chunk(list(range(1, N+1)), num_workers)

            queue = Queue()
            for i in range(0, num_workers):
                worker = CollatzWorker(queue=queue, numbers=chunks[i], idx=i)
                worker.start()
                workers.append(worker)

            results = [queue.get() for worker in workers]
            [worker.join() for worker in workers]

            self.graph = ChainMap(*results)
