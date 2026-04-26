import sys

def check(n, array):
    mItems = [0] + array
    for i in range(1, n // 2 + 1):
        left = 2 * i
        right = 2 * i + 1
        if left <= n and mItems[i] > mItems[left]:
            return "NO"
        if right <= n and mItems[i] > mItems[right]:
            return "NO"
    return "YES"

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    lst = [int(x) for x in input_data[1:n+1]]
    print(check(n, lst))
if __name__ == '__main__':
    main()