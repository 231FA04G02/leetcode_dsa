class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for ch in ransomNote:
            count[ch] = count.get(ch, 0) + 1

        freq = {}
        for ch in magazine:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in count:
            if freq.get(ch, 0) < count[ch]:
                return False

        return True
