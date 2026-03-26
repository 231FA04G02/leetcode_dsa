class Solution:
    def sortString(self, s):
        return "".join(sorted(s))   # fix

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}

        for s in strs:
            key = self.sortString(s)
            if key in dict1:
                dict1[key].append(s)
            else:
                dict1[key] = [s]

        return list(dict1.values())