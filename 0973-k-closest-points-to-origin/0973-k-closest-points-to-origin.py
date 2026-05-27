import heapq
class Solution:
    def kClosest(self, points, k):
        heap = []
        for (x, y) in points:
            dist = x*x + y*y
            heapq.heappush(heap, (dist, x, y))
        res = []
        for i in range(k):
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])
        return res
