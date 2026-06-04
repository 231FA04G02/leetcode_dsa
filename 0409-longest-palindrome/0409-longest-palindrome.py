from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0

        for count in Counter(s).values():
            ans += count // 2 * 2
            if ans % 2 == 0 and count % 2 == 1:
                ans += 1

        return ans