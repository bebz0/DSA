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
    def __init__(self):
        self.nodes = {}

    def add_edge(self, u, v):
        if u not in self.nodes:
            self.nodes[u] = Node(u)
        if v not in self.nodes:
            self.nodes[v] = Node(v)
        self.nodes[u].links.append(v)
        self.nodes[v].links.append(u)

    def __getitem__(self, key):
        if key not in self.nodes:
            self.nodes[key] = Node(key)
        return self.nodes[key]

def solve(g, starts):
    q = Queue()
    times = {}
    
    for p in starts:
        q.enqueue(p)
        times[p] = 0
        
    max_t = 0
    last_v = min(starts)
    
    while not q.empty():
        curr = q.dequeue()
        t = times[curr]
        
        if t > max_t:
            max_t = t
            last_v = curr
        elif t == max_t:
            if curr < last_v:
                last_v = curr
                
        for nxt in g[curr].neighbors():
            if nxt not in times:
                times[nxt] = t + 1
                q.enqueue(nxt)
                
    return max_t, last_v

def main():
    data = sys.stdin.read().split()
    if not data:
        return
        
    n = int(data[0])
    m = int(data[1])
    
    g = Graph()
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        g.add_edge(u, v)
        idx += 2
        
    k = int(data[idx])
    idx += 1
    
    starts = []
    for _ in range(k):
        starts.append(int(data[idx]))
        idx += 1
        
    max_t, last_v = solve(g, starts)
    
    print(max_t)
    print(last_v)

if __name__ == "__main__":
    main()