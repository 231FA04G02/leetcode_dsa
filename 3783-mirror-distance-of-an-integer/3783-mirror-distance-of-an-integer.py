class Solution:
    def mirrorDistance(self, n: int) -> int:
        if n <= 9:
            return 0
        
        rev = int(str(n)[::-1])
        return abs(n - rev)