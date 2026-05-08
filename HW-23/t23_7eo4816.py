import sys

class Queue:
    def __init__(self):
        self.items = []
        self.head = 0
        
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        res = self.items[self.head]
        self.head += 1
        return res
        
    def empty(self):
        return self.head == len(self.items)

class Node:
    def __init__(self, key):
        self.key = key
        self.links = []

    def neighbors(self):
        return self.links

class Graph:
    def __init__(self, n):
        self.nodes = [None] + [Node(i) for i in range(1, n + 1)]

    def add_edge(self, u, v):
        self.nodes[u].links.append(v)
        self.nodes[v].links.append(u)

    def __getitem__(self, key):
        return self.nodes[key]

def find_components(g, n):
    visited = [False] * (n + 1)
    all_components = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            current_component = []
            q = Queue()
            
            q.enqueue(i)
            visited[i] = True
            
            while not q.empty():
                curr = q.dequeue()
                current_component.append(curr)
                
                for nxt in g[curr].neighbors():
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.enqueue(nxt)
                        
            all_components.append(current_component)
            
    return all_components

def main():
    data = sys.stdin.read().split()
    if not data:
        return
        
    n = int(data[0])
    m = int(data[1])
    
    g = Graph(n)
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        g.add_edge(u, v)
        idx += 2
        
    components = find_components(g, n)
    
    out = [str(len(components))]
    for comp in components:
        out.append(str(len(comp)))
        out.append(" ".join(map(str, comp)))
        
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()