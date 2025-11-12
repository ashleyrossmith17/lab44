from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start):
        visited = set()
        stack = [start]
        result = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return result



g = Graph()


for i in range(9):
    g.add_edge(i, i + 1)


g.add_edge(0, 5)
g.add_edge(3, 8)
g.add_edge(2, 7)

print("Граф создан!")
print("Вершины:", list(g.graph.keys()))
print("Соседи:")
for node in sorted(g.graph.keys()):
    print(f"{node}: {g.graph[node]}")

print("\nDFS от 0:", g.dfs(0))
print("BFS от 0:", g.bfs(0))