import sys

def get_key(student):
    clas, surname = student[2], student[0]
    return (int(clas[:-1]), clas[-1], surname)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if get_key(arr[j]) > get_key(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

data = sys.stdin.read().split()
if data:
    n = int(data[0])
    students = [data[i:i+4] for i in range(1, 4 * n, 4)]
    bubble_sort(students)
    
    for s in students:
        print(f"{s[2]} {s[0]} {s[1]} {s[3]}")