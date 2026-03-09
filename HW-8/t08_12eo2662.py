import sys

def my_sort(arr):
    n = len(arr)
    target_idx = 0
    moves = 0
    
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            if target_idx == i:
                target_idx = min_idx
                moves += 1
            elif target_idx == min_idx:
                target_idx = i
                moves += 1
    return moves

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
        
    n = int(data[0])
    arr = [int(x) for x in data[1:n+1]]
    res = my_sort(arr)
    print(res)

if __name__ == "__main__":
    solve()