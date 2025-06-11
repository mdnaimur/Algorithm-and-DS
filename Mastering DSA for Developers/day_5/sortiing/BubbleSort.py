import random
import time


def bubbleSortBad(arr):
    print("Bubble sort bad")
    countBad = 0
    for i in range(len(arr)):
        for j in range(len(arr) - 1):  # check arr -1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            countBad += 1
    print("Operation Count Bad Approch : ", countBad)
    return arr


def bubbleSortGood(arr):
    print("Bubble sort good")
    n = len(arr)
    countGood = 0
    for i in range(n):
        swap = False
        for j in range(0, n - 1 - i):
            countGood += 1
            # print(f"Comparing: {arr[j]} and {arr[j + 1]}")
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
                # print(f"Swapped: {arr[j]} and {arr[j + 1]}")
        if not swap:
            break
    print(f"Total comparisons (better): {countGood}")

    return arr


def generate_random_array(length=9000):
    return [random.randint(11, 999) for _ in range(length)]


# Generate random array
random_array = generate_random_array()

# Make separate copies to avoid in-place sorting conflict
arr_bad = random_array.copy()
arr_good = random_array.copy()

# Time bad sort
start_bad = time.perf_counter()
bubbleSortBad(arr_bad)
end_bad = time.perf_counter()
print(f"⏱ Time taken (Bad): {end_bad - start_bad:.4f} seconds")

# Time good sort
start_good = time.perf_counter()
bubbleSortGood(arr_good)
end_good = time.perf_counter()
print(f"⏱ Time taken (Good): {end_good - start_good:.4f} seconds")
# Print a small part of result to verify sorting
print("First 20 elements (Bad Sort):", arr_bad[:20])
print("First 20 elements (Good Sort):", arr_good[:20])

print("_" * 60)
print("Now time save", (end_bad - start_bad) - (end_good - start_good))
