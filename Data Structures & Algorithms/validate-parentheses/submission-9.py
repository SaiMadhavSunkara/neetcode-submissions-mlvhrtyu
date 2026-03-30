class Solution:
    def isValid(self, s: str) -> bool:
        stack = ['0']

        for i in range(len(s)):
            if s[i] == ']' and stack[-1] == '[':
                stack.pop()
            elif s[i] == '}' and stack[-1] == '{':
                stack.pop()
            elif s[i] == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s[i])
        stack.pop(0)
        if not stack:
            return True
        else:
            return False
                
