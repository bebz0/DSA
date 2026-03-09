import sys

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        lefthalf = array[:mid]
        righthalf = array[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i][0] <= righthalf[j][0]:
                array[k] = lefthalf[i]
                i += 1
            else:
                array[k] = righthalf[j]
                j += 1
            k += 1
            
        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i += 1
            k += 1
            
        while j < len(righthalf):
            array[k] = righthalf[j]
            j += 1
            k += 1

data = sys.stdin.read().split()

if data:
    n = int(data[0])
    
    lst = []
    idx = 1
    for _ in range(n):
        lst.append((int(data[idx]), int(data[idx+1])))
        idx += 2
    merge_sort(lst)
    for r in lst:
        print(f"{r[0]} {r[1]}")