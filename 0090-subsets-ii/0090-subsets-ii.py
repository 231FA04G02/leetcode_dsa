class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []

        def solve(sub, start):
            res.append(sub[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                sub.append(nums[i])
                solve(sub, i + 1)
                sub.pop()

        solve([], 0)
        return res