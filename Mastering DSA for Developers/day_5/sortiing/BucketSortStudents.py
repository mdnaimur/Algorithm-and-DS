from math import floor
from pprint import pprint


def bucketSortForStudents(students):
    if not students:
        return []

    n = len(students) // 2 or 1
    buckets = [[] for _ in range(n)]

    for student in students:
        index = floor(student["score"] / (100 / n))
        index = min(index, n - 1)
        print(
            f"Placing {student['name']} (score: {student['score']}) in bucket {index}")
        buckets[index].append(student)

    print("\nBuckets before sorting:")
    for i, bucket in enumerate(buckets):
        print(f"Bucket {i}:")
        pprint(bucket)

    sorted_students = []
    for bucket in buckets:
        sorted_bucket = sorted(bucket, key=lambda s: s["score"])
        sorted_students.extend(sorted_bucket)

    print("\nFinal sorted students:")
    pprint(sorted_students)
    return sorted_students


students = [
    {"name": "Alice", "roll": 1, "score": 76},
    {"name": "Bob", "roll": 2, "score": 85},
    {"name": "Charlie", "roll": 3, "score": 45},
    {"name": "David", "roll": 4, "score": 89},
    {"name": "Emma", "roll": 5, "score": 67},
    {"name": "Frank", "roll": 6, "score": 72},
    {"name": "Grace", "roll": 7, "score": 83},
    {"name": "Henry", "roll": 8, "score": 38},
    {"name": "Ivy", "roll": 9, "score": 77},
    {"name": "Jack", "roll": 10, "score": 90},
    {"name": "Kate", "roll": 11, "score": 55},
    {"name": "Liam", "roll": 12, "score": 69},
    {"name": "Mia", "roll": 13, "score": 81},
    {"name": "Noah", "roll": 14, "score": 33},
    {"name": "Olivia", "roll": 15, "score": 88},
    {"name": "Peter", "roll": 16, "score": 73},
    {"name": "Quinn", "roll": 17, "score": 61},
    {"name": "Ryan", "roll": 18, "score": 79},
    {"name": "Sarah", "roll": 19, "score": 66},
    {"name": "Tom", "roll": 20, "score": 44},
    {"name": "Uma", "roll": 21, "score": 87},
    {"name": "Victor", "roll": 22, "score": 71},
    {"name": "Wendy", "roll": 23, "score": 82},
    {"name": "Xavier", "roll": 24, "score": 58},
    {"name": "Yara", "roll": 25, "score": 75},
    {"name": "Zack", "roll": 26, "score": 63},
    {"name": "Amy", "roll": 27, "score": 86},
    {"name": "Ben", "roll": 28, "score": 42},
    {"name": "Chloe", "roll": 29, "score": 78},
    {"name": "Dan", "roll": 30, "score": 70},
    {"name": "Eva", "roll": 31, "score": 84},
    {"name": "Felix", "roll": 32, "score": 51},
    {"name": "Gina", "roll": 33, "score": 74},
    {"name": "Hugo", "roll": 34, "score": 39},
    {"name": "Iris", "roll": 35, "score": 80},
    {"name": "Jake", "roll": 36, "score": 57},
    {"name": "Kim", "roll": 37, "score": 68},
    {"name": "Leo", "roll": 38, "score": 47},
    {"name": "Maya", "roll": 39, "score": 85},
    {"name": "Nick", "roll": 40, "score": 62},
    {"name": "Olive", "roll": 41, "score": 49},
    {"name": "Paul", "roll": 42, "score": 77},
    {"name": "Rose", "roll": 43, "score": 36},
    {"name": "Sam", "roll": 44, "score": 88},
    {"name": "Tina", "roll": 45, "score": 54},
    {"name": "Uri", "roll": 46, "score": 65},
    {"name": "Vera", "roll": 47, "score": 43},
    {"name": "Will", "roll": 48, "score": 59},
    {"name": "Xena", "roll": 49, "score": 41},
    {"name": "Yuki", "roll": 50, "score": 52},
]

sorted_students = bucketSortForStudents(students)

print("\n🎯 Only Scores:")
for s in sorted_students:
    print(s["score"])

print("\n👤 Name and Score:")
for s in sorted_students:
    print(f"{s['name']} - {s['score']}")

print("\n🧾 Roll and Score:")
for s in sorted_students:
    print(f"Roll {s['roll']} - {s['score']}")
