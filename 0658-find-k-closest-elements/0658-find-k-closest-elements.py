import heapq

class Solution:
    def findClosestElements(self, arr, k, x):
        heap = []

        for num in arr:
            heapq.heappush(heap, (abs(num - x), num))

        res = []

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return sorted(res)