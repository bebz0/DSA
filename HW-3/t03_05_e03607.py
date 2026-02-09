import sys
while True:
    try:
        line=sys.stdin.readline()
        if not line:
            break

        n = int(line.strip())
        arr = list(map(int, sys.stdin.readline().split()))
        a, b = map(int, sys.stdin.readline().split())
        print(sum(a<=x<=b for x in arr))  # лінійний пошук
        
    except(IndexError, ValueError):
        break

