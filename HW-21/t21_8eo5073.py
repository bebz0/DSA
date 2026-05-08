import sys

class Graph:
    def __init__(self, n):
        self.n = n
        self.matrix = [[0] * n for _ in range(n)]
        self.has_multiedges = False

    def add_edge(self, u, v):
        if self.matrix[u][v] > 0:
            self.has_multiedges = True
        self.matrix[u][v] += 1

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
        
    if g.has_multiedges:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()