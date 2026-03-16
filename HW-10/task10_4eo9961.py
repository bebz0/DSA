import sys

def solve(n, k):
    def backtrack(seq):
        if len(seq) == k:
            print(*seq)
            return
        
        for num in range(1, n + 1):
            if num not in seq:
                backtrack(seq + [num])

    backtrack([])

def main():
    n, k = map(int, sys.stdin.read().split())
    solve(n, k)

if __name__ == "__main__":
    main()