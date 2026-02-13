def f(x):
    return x**3 + 4 * x**2 + x -6

def solve(c=0.0, a=0.0, b=2.0, tolerance=1e-7):
    l=a
    r=b
    while (r-l)>tolerance:
        m=(r+l)/2.0
        if f(m)<c:
            l=m
        else:
            r=m

    return (r+l)/ 2.0

if __name__=="__main__":
    print(f'{solve():.7f}')