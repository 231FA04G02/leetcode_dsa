class Solution:
    def maxSubArray(self, nums):
        left = 0
        curr_sum = 0
        max_sum = float('-inf')

        for right in range(len(nums)):
            curr_sum += nums[right]
            max_sum = max(max_sum, curr_sum)

            while curr_sum < 0 and left <= right:
                curr_sum -= nums[left]
                left += 1

        return max_sum