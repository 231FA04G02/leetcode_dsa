from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = Counter(nums)
        ans = []
        for val, count in freq.items():
            if count > n // 3:
                ans.append(val)

        return ans