# 744. Find Smallest Letter Greater Than Target
# You are given an array of characters letters that is sorted in non-decreasing order, and a character target.
# There are at least two different characters in letters.
# Return the smallest character in letters that is lexicographically greater than target.
# If such a character does not exist, return the first character in letters.
# 1. Input: letters = ["c","f","j"], target = "a", Output: "c"
# Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
# 2. Input: letters = ["c","f","j"], target = "c", Output: "f"
# Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
# 3. Input: letters = ["x","x","y","y"], target = "z", Output: "x"
# Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].

class Solution:
    def nextGreatestLetters(self, letters, target):
        if target >= letters[-1] or target < letters[0]:
            return letters[0]

        low = 0
        high = len(letters) - 1

        while low <= high:
            mid = (low + high) // 2
            if target < mid[letters]:
                high = mid - 1
            elif target > mid[letters]:
                low = mid + 1
        return letters[low]

solution = Solution()
result = solution.nextGreatestLetters(["x", "x", "y", "y"], "z")
print(result)
# Output: 'X'
