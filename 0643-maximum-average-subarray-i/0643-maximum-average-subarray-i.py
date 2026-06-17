class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowsum=sum(nums[:k])
        currentsum=windowsum
        for i in range(k,len(nums)):
            windowsum+=nums[i]-nums[i-k]
            currentsum=max(currentsum,windowsum)
        return currentsum/k