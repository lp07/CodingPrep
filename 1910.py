# 1910. Remove All Occurrence of a Substring
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []  # To keep track of the characters in s
        for char in s:
            stack.append(char)
            if len(stack) >= len(part) and ''.join(stack[-len(part):]) == part:
                # Remove the occurrence of the substring
                for i in range(len(part)):
                    stack.pop()
        return ''.join(stack)
