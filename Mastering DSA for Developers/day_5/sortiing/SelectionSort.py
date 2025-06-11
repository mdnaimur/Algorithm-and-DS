import random


def selectionSort(arr):
    n = len(arr)
    for i in range(n - 1):
        minIndex = i
        for j in range(i, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if minIndex != i:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr


def generate_random_array(length=10000):
    return [random.randint(1, 100) for _ in range(length)]


arr = generate_random_array(10000)
print('Before Sorting:', arr)

print('\n--------------------------------\n')

sorted_arr = selectionSort(arr)
print('After Sorting:', sorted_arr)
