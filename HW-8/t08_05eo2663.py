def bulb_sort():
    n = int(input())
    arr = list(map(int, input().split()))
    swaps = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1            
    print(swaps)

if __name__ == "__main__":
    bulb_sort()