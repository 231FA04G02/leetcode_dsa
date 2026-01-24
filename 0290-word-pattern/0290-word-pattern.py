class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()
        
        if len(pattern) != len(word):
            return False
        
        ptw = {}
        wtp = {}

        for c1, c2 in zip(pattern, word):
            if c1 in ptw and ptw[c1] != c2:
                return False
            if c2 in wtp and wtp[c2] != c1:
                return False

            ptw[c1] = c2
            wtp[c2] = c1

        return True
