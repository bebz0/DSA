def lower_bound(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= x:
            right = mid
        else:
            left = mid + 1
    return left

def upper_bound(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > x:
            right = mid
        else:
            left = mid + 1
    return left

n = int(input())
arr_collection = list(map(int, input().split()))
m = int(input())
arr_check = list(map(int, input().split()))

for x in arr_check:
    l_idx = lower_bound(arr_collection, x)
    r_idx = upper_bound(arr_collection, x)
    print(r_idx - l_idx)