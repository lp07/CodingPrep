# 1768. Merge Strings Alternately
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
# starting with word1. f a string is longer than the other,
# append the additional letters onto the end of the merged string.
# Return the merged string.
# Example 1:
# Input: word1 = "abc", word2 = "pqr", Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:
# Input: word1 = "ab", word2 = "pqrs", Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b
# word2:    p   q   r   s
# merged: a p b q   r   s

class Solution:
    def mergeAlternately(self, word1, word2):
        result = []
        w = min(len(word1), len(word2))
        for i in range(w):
            result.append(word1[i] + word2[i])
        return ''.join(result) + (word1[w:] + (word2[w:]))

solution = Solution()
word1 = "abc"
word2 = "pqr"
final_result = solution.mergeAlternately(word1, word2)
print(final_result)

# output: apbqcr


