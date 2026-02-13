def f(x):
    return x**3+ x + 1

def solve(c=5.0, a=0.0, b=10.0, tolerance=1e-7):
    l = a
    r = b
    while (r-l)>tolerance:
        m=(r+l) / 2.0
        if f(m) < c:
            l = m
        else:
            r = m
    
    return (r+l)/2.0


if __name__ == "__main__":
    print(solve())