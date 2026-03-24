class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if n == 0:
                return 1
            
            a = power(x, n // 2)
            
            if n % 2 == 0:
                return a * a
            else:
                return a * a * x
        
        if n < 0:
            return 1 / power(x, -n)
        
        return power(x, n)
        