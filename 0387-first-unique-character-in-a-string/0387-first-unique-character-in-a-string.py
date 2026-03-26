# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         for i in range(len(s)):
#             unique = True
#             for j in range(len(s)):
#                 if i != j and s[i] == s[j]:
#                     unique = False
#                     break
#             if unique == True:
#                 return i
#         return -1 



class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1