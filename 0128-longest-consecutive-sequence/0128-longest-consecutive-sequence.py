class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        arr = sorted(set(nums))
        longest = 1
        count = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1] + 1:
                count += 1
            else:
                longest = max(longest, count)
                count = 1
        return max(longest, count)
        
        