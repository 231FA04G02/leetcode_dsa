class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]

        sum2 = 0
        for i in range(len(nums)):
            n = nums[i]
            while n > 0:
                sum2 += n % 10
                n //= 10

        return sum - sum2
