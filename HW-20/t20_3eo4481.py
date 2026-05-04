import math
import sys

class SegmentTree:
    def __init__(self, array):
        k = len(array)
        n = 1 if k <= 1 else (1 << int(math.log2(k - 1)) + 1) 
        
        self.items = 2 * n * [0] 

        for i in range(k):
            self.items[n + i] = array[i]

        for i in range(n - 1, 0, -1):
            self.items[i] = math.gcd(self.items[2 * i], self.items[2 * i + 1])
        self.size = n


    def update(self, pos, x):
        pos += self.size
        self.items[pos] = x

        i = pos // 2 
        while i > 0:
            self.items[i] = math.gcd(self.items[2 * i], self.items[2 * i + 1])
            i //= 2


    def get_gcd(self, left, right):
        left += self.size
        right += self.size
        res = 0
        while left <= right:
            if left % 2 == 1:
                res = math.gcd(res, self.items[left])
            if right % 2 == 0:
                res = math.gcd(res, self.items[right])
            left = (left + 1) // 2
            right = (right - 1) // 2
        return res


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    array = [int(x) for x in input_data[1:n+1]]
    tree = SegmentTree(array)
    m = int(input_data[n+1])
    idx = n + 2
    out = []
    for _ in range(m):
        q = int(input_data[idx])
        l = int(input_data[idx+1])
        r = int(input_data[idx+2])
        idx += 3
        
        if q == 1:
            result = tree.get_gcd(l - 1, r - 1)
            out.append(str(result))
        elif q == 2:
            tree.update(l - 1, r)
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()