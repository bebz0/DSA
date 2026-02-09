def search(arr, n):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (right+left)//2
        if arr[mid] == n:
            return 'YES'
        elif arr[mid] < n:
            left = mid+1
        else:
            right = mid -1
    return 'NO'

n = int(input())
arr_collection = list(map(int, input().split()))
m = int(input())
arr_check = list(map(int, input().split()))

for i in arr_check:
    print(search(arr_collection, i))