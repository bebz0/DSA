import sys

class Graph:
    def __init__(self, n):
        self.n = n
        self.matrix = [[0] * n for _ in range(n)]

    def add_edge(self, u, v):
        if u != v:
            self.matrix[u][v] = 1
            self.matrix[v][u] = 1

    def is_complete(self):
        for i in range(self.n):
            for j in range(self.n):
                if i != j and self.matrix[i][j] == 0:
                    return False
        return True

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    g = Graph(n)
    
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        g.add_edge(u, v)
        idx += 2
        
    if g.is_complete():
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()