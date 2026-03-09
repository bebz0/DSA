def insertion_sort(array):
    n = len(array)
    for index in range(1, n):
        curr_value = array[index]
        pos = index        
        while pos > 0:
            if array[pos - 1] > curr_value:
                array[pos] = array[pos - 1]
            else:
                break
            pos -= 1
            
        array[pos] = curr_value
        if pos != index:
            print(*array)

n = int(input().strip())
arr = list(map(int, input().split()))
insertion_sort(arr)