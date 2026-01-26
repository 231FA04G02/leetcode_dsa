class Solution:
    def isHappy(self, n: int) -> bool:
        dict={}
        
        while n!=1:
            if n in dict:
                return False

            dict[n]=1

            s=0
            for digit in str(n):
                s+=int(digit)**2
                n=s
        return True


            
