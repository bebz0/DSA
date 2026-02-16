# example below, replace it with your solution
def f(x):
    return x*x + x ** 0.5

def solve(c, a=1.0, b=10**10):
    l = a
    r = b
    m = (l+r) / 2.0
    while l!=m and m!=r:
        if f(m)<c:
            l = m
        else:
            r = m
        m = (l+r) / 2.0
    
    return (l+r)/2.0



c = float(input())
print(f'{solve(c):.7f}')