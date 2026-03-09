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

n = int(input().strip())

lst = []
for _ in range(n):
    h, m, s = map(int, input().split())
    lst.append((h, m, s))

insertion_sort(lst)

for h, m, s in lst:
    print(f"{h} {m} {s}")