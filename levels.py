from collatz import CollatzGraph


graph = CollatzGraph()

graph.graph[16] = [8]
for i in range(10):
    graph.add_level()

print(graph)