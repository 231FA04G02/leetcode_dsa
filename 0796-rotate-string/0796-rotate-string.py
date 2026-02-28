class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # return goal in (s+s)[1:-1]
        
        for i in range(len(s)):
            temp=s[1:len(s)]
            temp+=s[0]
            s=temp

            if s==goal:
                return True
        return False

    

        
    
        
           
        