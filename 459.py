# 459. Repeated Substring Pattern
# Given a string s, check if it can be constructed by taking a substring of it
# and appending multiple copies of the substring together.
# 1. s = "abab" , o/p = True
# 2. s = "aba" , o/p = False
# 3. "abcabcabc", o/p = True
# 4. "abac", o/p = False
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Iterate over all possible substring length from 1 to len(s) // 2
        for i in range(1, len(s) // 2 + 1):
            # check if the first i character of s repeated multiple times
            # equal the original string
            if s[:i] * (len(s) // 2) == s:
                return True
            # i fno repeated string found, return False
        return False    