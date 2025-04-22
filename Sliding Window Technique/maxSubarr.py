def max_subarray_sum(nums, k):
    max_sum = float('-inf')
    window_sum = sum(nums[:k])

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


# Example usage

nums = [2, 1, 5, 1, 3, 2]
windwo_size = 3
resutl = max_subarray_sum(nums, windwo_size)
print("maximum subarray sum: ", resutl)
