from math import floor


def BinarySearch(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = floor((low + high) // 2)
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 70

index = BinarySearch(arr, target)
print(index)
