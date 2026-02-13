import math

def f(x):
    return math.sin(x) - x/3.0

def solve(c=0.0, a=1.6, b=3.0, tolerance=1e-7):
    l = a
    r = b
    while (r - l) > tolerance:
        m = (l + r) / 2.0
        if f(m) > c: 
            l = m
        else:
            r = m
            
    return (r+l)/2.0

if __name__ == "__main__":
    print(f'{solve():.7f}')