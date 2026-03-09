import sys

def get_weight(num):
    return sum(int(dig) for dig in str(num))

def is_less(a, b):
    w_a = get_weight(a)
    w_b = get_weight(b)
    
    if w_a != w_b:
        return w_a < w_b
        
    return str(a) < str(b)

def selection_sort(array):
    length = len(array)
    for i in range(length - 1, 0, -1):
        maxpos = 0
        for j in range(1, i + 1):
            if is_less(array[maxpos], array[j]):
                maxpos = j
        array[i], array[maxpos] = array[maxpos], array[i]

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    arr = list(range(1, n + 1))
    selection_sort(arr)
    pos_k = arr.index(k) + 1
    val_k = arr[k - 1]
    print(pos_k)
    print(val_k)

if __name__ == "__main__":
    solve()