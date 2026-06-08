class Solution:
    def subsets(self, nums):
        res = []

        def solve(sub, start):
            res.append(sub[:])

            for i in range(start, len(nums)):
                sub.append(nums[i])
                solve(sub, i + 1)
                sub.pop()

        solve([], 0)
        return res