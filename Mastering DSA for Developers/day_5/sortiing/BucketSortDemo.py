def bucketSortObj(arr, key):
    n = len(arr)
    if n <= 0:
        return arr

    buckets = [[] for _ in range(10)]

    for item in arr:
        value = item[key]
        index = int((value / 100) * 10)
        print(f"index is {index} for value of {value}")
        if index == 10:
            index = 9
        buckets[index].append(item)

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket, key=lambda x: x[key]))

    return sorted_arr


students = [
    {"name": "Alice", "score": 91},
    {"name": "Bob", "score": 75},
    {"name": "Charlie", "score": 85},
    {"name": "David", "score": 60},
    {"name": "Eva", "score": 99},
    {"name": "Frank", "score": 45}
]

sorted_students = bucketSortObj(students, "score")

for student in sorted_students:
    print(student)
