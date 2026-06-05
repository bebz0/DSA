class DSU:
    def __init__(self, size):
        self.parent = list(range(size + 1))
        self.rank = [0] * (size + 1)

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def unite(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return False

        if self.rank[a] < self.rank[b]:
            a, b = b, a

        self.parent[b] = a

        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1

        return True


tests = int(input())

for _ in range(tests):
    n, m, p, q = map(int, input().split())

    roads = []
    needed_edge = None

    for _ in range(m):
        city1, city2, length = map(int, input().split())

        roads.append((length, city1, city2))

        if (city1 == p and city2 == q) or (city1 == q and city2 == p):
            needed_edge = (city1, city2, length)

    roads.sort()

    dsu = DSU(n)
    answer = "NO"

    for length, city1, city2 in roads:
        if dsu.unite(city1, city2):
            if needed_edge is not None:
                a, b, w = needed_edge

                if length == w and (
                    (city1 == a and city2 == b) or
                    (city1 == b and city2 == a)
                ):
                    answer = "YES"
                    break

    print(answer)