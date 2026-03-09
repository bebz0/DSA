import sys

def qsort(array, a, b):
    if a >= b: 
        return
    pivot = array[a + (b - a) // 2]
    left = a
    right = b 

    while True:
        while array[left] < pivot:
            left += 1

        while pivot < array[right]:
            right -= 1

        if left >= right:
            break
        array[left], array[right] = array[right], array[left] 
        left += 1                   
        right -= 1                  
    qsort(array, a, right)
    qsort(array, right + 1, b)

data = sys.stdin.read().split()

if data:
    n = int(data[0])
    arr = [int(x) for x in data[1:n+1]]
    if n > 0:
        qsort(arr, 0, n - 1)
    
    print(*(arr))