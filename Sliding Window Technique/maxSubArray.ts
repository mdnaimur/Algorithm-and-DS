

function maxSubArraySum(nums: number[], k: number): number {
    let maxSum = Number.MIN_SAFE_INTEGER;
    let windowSum = 0;

    for (let i = 0; i < k; i++) {
        windowSum += nums[i];                                
    }

    maxSum = windowSum;
    console.log('maxsum is : ',maxSum)

    for (let i = k; i < nums.length; i++) {
        windowSum += nums[i] - nums[i - k];
        maxSum = Math.max(maxSum, windowSum);
    }

    return maxSum;
}

const nums: number[] = [2, 1, 5, 1, 3, 2]; 
const windowSize: number = 2;
const result: number = maxSubArraySum(nums, windowSize);

console.log("Maximum subarray sum:", result);


