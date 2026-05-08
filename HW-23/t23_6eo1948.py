import sys

sys.setrecursionlimit(200000)

WHITE = 0
GRAY = 1
BLACK = 2

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def empty(self):
        return len(self.items) == 0

class Node:
    def __init__(self, key):
        self.key = key
        self.state = WHITE
        self.links = []

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def neighbors(self):
        return self.links

class Graph:
    def __init__(self, n):
        self.nodes = {i: Node(i) for i in range(1, n + 1)}

    def add_edge(self, u, v):
        self.nodes[u].links.append(v)

    def __getitem__(self, key):
        return self.nodes[key]

    def get_nodes(self):
        return self.nodes.keys()

class CycleException(Exception):
    pass

def dfs(g, v_key, stack):
    node = g[v_key]
    
    if node.get_state() == BLACK:
        return
        
    if node.get_state() == GRAY:
        raise CycleException
        
    node.set_state(GRAY)
    
    for nxt in node.neighbors():
        dfs(g, nxt, stack)
        
    node.set_state(BLACK)
    stack.push(v_key)

def solve(g):
    stack = Stack()
    
    for v_key in g.get_nodes():
        if g[v_key].get_state() == WHITE:
            try:
                dfs(g, v_key, stack)
            except CycleException:
                return None
                
    res = []
    while not stack.empty():
        res.append(stack.pop())
        
    return res

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
        
    res = solve(g)
    
    if res is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write(" ".join(map(str, res)) + "\n")

if __name__ == "__main__":
    main()