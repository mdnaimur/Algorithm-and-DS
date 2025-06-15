
def LinerSerch(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i

    return -1


array = [5, 3, 8, 4, 2]
target = 4
result = LinerSerch(array, target)
if result != -1:
    print(f"Result found index {result}")
else:
    print("Not found... Sorry")
