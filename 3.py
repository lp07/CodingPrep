class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        res = 0
        i = 0
        for j in range(0, len(s)):
            if s[j] in dict:
                i = max(i, (dict[s[j]] + 1))
            res = max(res, (j - i + 1))
            dict[s[j]] = j   
        return res    