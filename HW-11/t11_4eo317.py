import sys
sys.set_int_max_str_digits(300000)
def foo(x, y):
    if x < 5000 or y < 5000:
        return x * y

    m = max(x.bit_length(), y.bit_length()) // 2
    mask = (1 << m) - 1
    
    x0 = x & mask
    x1 = x >> m
    
    y0 = y & mask
    y1 = y >> m
    
    z2 = foo(x1, y1)
    z0 = foo(x0, y0)
    z1 = foo(x1 + x0, y1 + y0) - z2 - z0
    
    return (z2 << (2 * m)) + (z1 << m) + z0

def main():
    input_data = sys.stdin.read().split()
    a = int(input_data[0])
    b = int(input_data[1])
    print(foo(a, b))

if __name__ == '__main__':
    sys.setrecursionlimit(2000)
    main()