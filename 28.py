# 28. Find the Index of the First Occurrence in a String

# Input: haystack = "sadbutsad", needle = "sad", Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Input: haystack = "leetcode", needle = "leeto", Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

# TC = O(n)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i

        return -1

s = Solution()
haystack = "sadbutsad"
needle = "sad"
print(s.strStr(haystack, needle)) 
# Output: 0

