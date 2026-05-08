import sys
class Graph:
    def __init__(self, n):
        self.n = n
        self.matrix = [[0] * n for _ in range(n)]

    def get_leaves_count(self):
        count = 0
        for row in self.matrix:
            if sum(row) == 1:
                count += 1
        return count

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    g = Graph(n)
    idx = 1
    for i in range(n):
        for j in range(n):
            g.matrix[i][j] = int(data[idx])
            idx += 1
            
    print(g.get_leaves_count())

if __name__ == '__main__':
    main()