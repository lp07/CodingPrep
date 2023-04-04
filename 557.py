# 557. Reverse Words in a String III
class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_words = [word[::-1] for word in s.split()]
        return " ".join(reversed_words)
