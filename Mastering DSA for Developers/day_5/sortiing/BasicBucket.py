

# Bucket sort

def bucketSort(array):
    bucket = []
    n = len(array)

    # create empty buckets
    for i in range(n):
        bucket.append([])
        # print(f"After create empty buckets = {bucket}")

    # Inserrt elements intor their respective buckts

    for j in array:
        # print(f"This is j = {j}")
        index_b = int(10 * j)
        if index_b > n:
            raise Exception("Index out of range ")
        print(f"index_b = {index_b}")
        bucket[index_b].append(j)
        print(f"buckett array: {bucket}")

    # Sort the elements  of each bucket
    print("______"*20)
    for i in range(n):
        bucket[i] = sorted(bucket[i])
        print(f"sorting buckt: {bucket[i]}")

    # Get the sorted Elements
    print("______"*20)
    k = 0

    for i in range(n):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            print(
                f"Sorting Array: arry[k] {array[k]} = bucket[i][j] {bucket[i][j]}")
            k += 1
    return array


array = [.45, .37, .31, .52, .30, .42, .51, .47]
array2 = [45, 37, 31, 52, 30, 42, 51, 47]


print("Sorted Array in descending order is")
print(bucketSort(array))
