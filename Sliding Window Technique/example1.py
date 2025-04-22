'''
Maximum sum subarray of size k

'''


def getMaxSum(arr, k):
    maxSum = 0
    windowSum = 0
    start = 0

    for i in range(len(arr)):
        windowSum += arr[i]
        print(f"Added arr[{i}] = {arr[i]}, windowSum = {windowSum}")

        # Check if the window size reached k
        if (i - start + 1) == k:
            maxSum = max(maxSum, windowSum)
            print(f"Window [{start}:{i}] -> maxSum updated to {maxSum}")

            # Slide the window forward
            windowSum -= arr[start]
            print(
                f"Subtracted arr[{start}] = {arr[start]}, new windowSum = {windowSum}")
            start += 1

    return maxSum


# Test case
arr = [3, 5, 2, 1, 7]
k = 2
result = getMaxSum(arr, k)
print(f"Maximum sum of any {k}-element subarray: {result}")
