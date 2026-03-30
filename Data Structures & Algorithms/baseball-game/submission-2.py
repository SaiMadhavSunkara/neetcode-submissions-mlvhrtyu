class Solution:
    def calPoints(self, operations: List[str]) -> int:
        i = 0
        new_stack = []
        while i < len(operations):
            if operations[i] == '+':
                new_stack.append(new_stack[-1] + new_stack[-2])
            elif operations[i] == 'C':
                new_stack.pop()
            elif operations[i] == 'D':
                new_stack.append(new_stack[-1]*2)        
            else:
                new_stack.append(int(operations[i]))
            i += 1
        return sum(new_stack)