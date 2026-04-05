import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    A = int(input_data[0])
    P = int(input_data[1])
    if A == 0:
        print("0")
        return
        
    stack = []
    while A > 0:
        rem = A % P
        stack.append(rem)
        A //= P
        
    res = []
    
    while len(stack) > 0:
        digit = stack.pop()
        
        if digit < 10:
            res.append(str(digit))
        else:
            res.append(f"[{digit}]")
    
    print("".join(res))

if __name__ == '__main__':
    solve()