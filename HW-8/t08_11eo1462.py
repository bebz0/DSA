import sys

def is_greater(a, b):
    last_a = a % 10
    last_b = b % 10
    if last_a != last_b:
        return last_a > last_b
    return a > b

def insertion_sort(array):
    n = len(array)
    for index in range(1, n):
        curr_value = array[index]
        pos = index
        while pos > 0 and is_greater(array[pos - 1], curr_value):
            array[pos] = array[pos - 1]
            pos -= 1
            
        array[pos] = curr_value

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
        
    n = int(data[0])
    nums = [int(x) for x in data[1:n+1]]
    insertion_sort(nums)
    print(*(nums))

if __name__ == "__main__":
    solve()