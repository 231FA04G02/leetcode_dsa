class Solution:
    def findLucky(self, arr: List[int]) -> int:
        fre = {}
        
        for i in arr:
            fre[i] = fre.get(i, 0) + 1
        
        ans = -1
        for num, count in fre.items():
            if num == count:
                ans = max(ans, num)
        
        return ans
