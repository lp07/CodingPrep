class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        parantheses = {'(': ')','{': '}', '[': ']' }
        for char in s:
            if char in parantheses:
                stack.append(char)
            elif len(stack) == 0 or char != parantheses[stack.pop()]:
                return False
        return len(stack) == 0