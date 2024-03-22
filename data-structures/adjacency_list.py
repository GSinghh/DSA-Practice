#Graph Implementation 

class Graph:
    def __init__(self) -> None:
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex1)
            self.graph[vertex2].append(vertex1)
    
    def display_graph(self):
        for vertex in self.graph:
            print("vertex -> ", self.graph[vertex])
            
    def bfs(self, start_vertex):
        visited = [False] * len(self.graph)
        distance = [0] * len(self.graph)
        queue = []
        queue.append(start_vertex)
        visited[start_vertex] = True
        distance[start_vertex] = 0
        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")
            for neighbor in self.graph[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    distance[neighbor] = distance[vertex] + 1 
        print("\nDistances:")
        print(distance)
        
    def dfs(self, start_vertex):
        visited = [False] * len(self.graph)
        self.dfs_helper(start_vertex, visited)
        
    def dfs_helper(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")
        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs_helper(neighbor,visited)
                
g = Graph()
g.add_vertex(0)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Graph:")
g.display_graph()

print("\nBFS:")
g.bfs(2)

print("\nDFS:")
g.dfs(2)