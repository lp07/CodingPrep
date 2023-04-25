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
        if len(needle) > len(haystack):
            return -1
        if needle == haystack[:len(needle)]:  # checks if the needle string is equal to the substring of the
            # haystack string from index 0 to the length of the needle string.
            return 0
        return -1
