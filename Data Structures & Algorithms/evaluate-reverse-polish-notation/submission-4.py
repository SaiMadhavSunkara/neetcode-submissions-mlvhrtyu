class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        temp = 0 
        if len(tokens) == 1:
            return int(tokens[0])
        def p(st, x):
            st.pop()
            st.pop()
            st.append(x)
        for i in tokens:
            temp = 0
            if i == '+':
                temp = stack[-2] + stack[-1]
                p(stack, temp)
            elif i == '-':
                temp = stack[-2] - stack[-1]
                p(stack, temp)
            elif i == '*':
                temp = stack[-2] * stack[-1]
                p(stack, temp)
            elif i == '/':
                temp = int(stack[-2] / stack[-1])
                p(stack, temp)
            else:
                stack.append(int(i))
        return temp

        