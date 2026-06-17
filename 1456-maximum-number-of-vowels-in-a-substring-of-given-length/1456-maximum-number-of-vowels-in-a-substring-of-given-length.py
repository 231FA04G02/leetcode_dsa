class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v={'a','e','i','o','u'}
        windowcount=0
        for i in range(k):
            if s[i] in v:
                windowcount+=1

        maximumcount=windowcount

        for i in range(k, len(s)):
            if s[i] in v:
                windowcount+=1
            if s[i-k] in v:
                windowcount-=1
        
            maximumcount=max(maximumcount,windowcount)
        return maximumcount