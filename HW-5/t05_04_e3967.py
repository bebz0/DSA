import sys

def check(lengths, k, m):
    if m == 0:
        return True
    count = 0
    for length in lengths:
        count += length // m
    return count >= k

def solve():
    try:
        input_data = sys.stdin.read().split()
        if not input_data:
            return
        n = int(input_data[0])
        k = int(input_data[1])
        lengths = [int(x) for x in input_data[2:]]
    except EOFError:
        return

    l = 0
    r = 10**7 + 1
    best = 0

    while l <= r:
        m = (l + r) // 2
        if m == 0:
            l = 1
            continue
            
        if check(lengths, k, m):
            best = m
            l = m + 1
        else:
            r = m - 1

    print(best)

if __name__ == "__main__":
    solve()