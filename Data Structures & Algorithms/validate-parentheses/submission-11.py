class Solution:
    def isValid(self, s: str) -> bool:
        stack = ['0']
        for i in s:
            if i == ']' and stack[-1] == '[':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            elif i == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        if len(stack) == 1:
            return True
        else:
            return False
                
