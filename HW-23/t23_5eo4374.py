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

    def add_edge(self, u, v, e_id):
        if u not in self.nodes:
            self.nodes[u] = Node(u)
        if v not in self.nodes:
            self.nodes[v] = Node(v)
        self.nodes[u].links.append((v, e_id))
        self.nodes[v].links.append((u, e_id))

    def __getitem__(self, key):
        if key not in self.nodes:
            self.nodes[key] = Node(key)
        return self.nodes[key]

def main():
    data = sys.stdin.read().split()
    if not data:
        return
        
    n = int(data[0])
    m = int(data[1])
    
    g = Graph()
    
    idx = 2
    for i in range(1, m + 1):
        u = int(data[idx])
        v = int(data[idx + 1])
        g.add_edge(u, v, i)
        idx += 2
        
    k = int(data[idx])
    idx += 1
    out = []
    for _ in range(k):
        c = int(data[idx])
        idx += 1
        ignored = set()
        for _ in range(c):
            ignored.add(int(data[idx]))
            idx += 1
            
        q = Queue()
        q.enqueue(1)
        
        visited = [False] * (n + 1)
        visited[1] = True
        count = 1
        while not q.empty():
            curr = q.dequeue()
            for nxt, e_id in g[curr].neighbors():
                if e_id not in ignored:
                    if not visited[nxt]:
                        visited[nxt] = True
                        count += 1
                        q.enqueue(nxt)
                        
        if count == n:
            out.append("Connected")
        else:
            out.append("Disconnected")
            
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()