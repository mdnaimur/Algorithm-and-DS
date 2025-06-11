import random


def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i - 1
        key = arr[i]
        while key < arr[j] and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"i = {i} j = {j} arr = {arr}\n")
        print("____" * 20)
    return arr


def generate_random_array(length=10000):
    return [random.randint(1, 100) for _ in range(length)]


arr = generate_random_array(8)
print('Before Sorting:', arr)

print('\n--------------------------------\n')

sorted_arr = insertionSort(arr)
print('After Sorting:', sorted_arr)
