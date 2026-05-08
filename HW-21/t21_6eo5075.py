import sys
class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = {}
    def add_neighbor(self, vertex_key, weight=1):
        self.neighbors[vertex_key] = weight

class Graph:
    def __init__(self, oriented=True):
        self.oriented = oriented
        self.vertices = {}
    def add_vertex(self, key):
        if key not in self.vertices:
            self.vertices[key] = Vertex(key)

    def add_edge(self, src, dest, weight=1):
        self.add_vertex(src)
        self.add_vertex(dest)
        self.vertices[src].add_neighbor(dest, weight)
        if not self.oriented:
            self.vertices[dest].add_neighbor(src, weight)

    def get_in_out_degrees(self, n):
        in_degrees = {i: 0 for i in range(1, n + 1)}
        out_degrees = {i: 0 for i in range(1, n + 1)}
        
        for key, vertex in self.vertices.items():
            out_degrees[key] = len(vertex.neighbors)            
            for neighbor in vertex.neighbors:
                in_degrees[neighbor] += 1
                
        return in_degrees, out_degrees

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    g = Graph(oriented=True)
    for i in range(1, n + 1):
        g.add_vertex(i)        
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        g.add_edge(u, v)
        idx += 2
        
    in_degrees, out_degrees = g.get_in_out_degrees(n)
    
    for i in range(1, n + 1):
        print(f"{in_degrees[i]} {out_degrees[i]}")

if __name__ == '__main__':
    main()