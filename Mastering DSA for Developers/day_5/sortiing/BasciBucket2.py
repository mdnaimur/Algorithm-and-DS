
def bucket_sort(arr):
    n = len(arr)
    if n <= 0:
        print("Empty array or invalid input.")
        return arr

    # Create Empty buckets:
    print(f"Original array: {arr}")
    buckets = [[] for _ in range(n)]
    print(f"Initialized {n} empty buckets.")
    # Put array elemets in different buckets
    print("______"*20)
    for i in range(n):
        index = int(arr[i] * n)
        print(f"Placing element {arr[i]} into bucket index {index}.")
        buckets[index].append(arr[i])

    # Print bucket contents before sorting
    print("______"*20)
    for i, bucket in enumerate(buckets):
        print(f"Bucket {i} before sorting: {bucket}")

    # sort individual buckets and  concatenate
    print("______"*20)
    sorted_array = []
    for bucket in buckets:
        sorted_bucket = sorted(bucket)
        print(f"Bucket {bucket} after sorting: {sorted_bucket}")
        sorted_array.extend(sorted(bucket))

    print(f"Final sorted array: {sorted_array}")
    return sorted_array


arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
arr2 = []
print(bucket_sort(arr))
