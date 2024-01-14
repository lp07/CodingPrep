# LeetCode 1071. Greatest Common Divisor of String

# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one
# or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

# Example 2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

# Example 3:
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        length_gcd = gcd(len(str1), len(str2))
        return str1[:length_gcd]

sol = Solution()
str1 = "ABABAB"
str2 = "AB"
result = sol.gcdOfStrings(str1, str2)
print(result)
# Output: "AB"
