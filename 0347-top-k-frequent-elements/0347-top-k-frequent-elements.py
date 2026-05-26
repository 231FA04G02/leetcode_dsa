import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        freq = Counter(nums)

        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (-count, num))

        res = []

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res