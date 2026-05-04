import math
import sys

class SegmentTree:
    def __init__(self, array):
        length = len(array)
        capacity = 1 if length <= 1 else (1 << int(math.log2(length - 1)) + 1)
        self.tree = [(float('inf'), float('-inf'))] * (2 * capacity)
        self.size = capacity
        for i in range(length):
            self.tree[capacity + i] = (array[i], array[i])
        for i in range(capacity - 1, 0, -1):
            left_min, left_max = self.tree[2 * i]
            right_min, right_max = self.tree[2 * i + 1]
            self.tree[i] = (min(left_min, right_min), max(left_max, right_max))

    def update(self, index, value):
        index += self.size
        self.tree[index] = (value, value)
        parent = index // 2
        while parent > 0:
            left_min, left_max = self.tree[2 * parent]
            right_min, right_max = self.tree[2 * parent + 1]
            self.tree[parent] = (min(left_min, right_min), max(left_max, right_max))
            parent //= 2

    def get_min_max(self, left, right):
        left += self.size
        right += self.size
        
        res_min = float('inf')
        res_max = float('-inf')
        while left <= right:
            if left % 2 == 1:
                res_min = min(res_min, self.tree[left][0])
                res_max = max(res_max, self.tree[left][1])
            if right % 2 == 0:
                res_min = min(res_min, self.tree[right][0])
                res_max = max(res_max, self.tree[right][1])
                
            left = (left + 1) // 2
            right = (right - 1) // 2
            
        return res_min, res_max


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    sigma_iterator = iter(input_data)
    n = int(next(sigma_iterator))
    array = [int(next(sigma_iterator)) for _ in range(n)]
    
    segment_tree = SegmentTree(array)
    
    m = int(next(sigma_iterator))
    results = []
    
    for _ in range(m):
        query_type = int(next(sigma_iterator))
        
        if query_type == 1:
            left = int(next(sigma_iterator)) - 1
            right = int(next(sigma_iterator)) - 1
            
            min_val, max_val = segment_tree.get_min_max(left, right)
            results.append("draw" if min_val == max_val else "wins")
            
        elif query_type == 2:
            index = int(next(sigma_iterator)) - 1
            value = int(next(sigma_iterator))
            
            segment_tree.update(index, value)
    sys.stdout.write('\n'.join(results) + '\n')


if __name__ == '__main__':
    solve()