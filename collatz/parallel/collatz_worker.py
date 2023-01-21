from multiprocessing import Process, Queue


class CollatzWorker(Process):
    def __init__(self, queue: Queue, numbers, idx=-1):
        super().__init__()
        self.queue = queue
        self.graph = dict()
        self.numbers = numbers
        self.idx = idx

    def run(self):
        #print(f'Started up worker {self.idx} for numbers: {self.numbers[:10]}...')
        for n in self.numbers:
            while n not in self.graph:
                if n % 2 == 0:
                    d = n//2
                else:
                    d = 3*n + 1
                self.graph[n] = [d]
                n = d
        #print(f'Finished worker {self.idx}')
        self.queue.put(self.graph)
