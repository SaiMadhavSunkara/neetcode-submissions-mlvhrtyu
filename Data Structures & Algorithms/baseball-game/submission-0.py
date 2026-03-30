class Solution:
    def calPoints(self, operations: List[str]) -> int:
        table = []
        j = 0
        while j < len(operations):
            if operations[j] == '+':
                table.append(int(table[-1])+int(table[-2]))
            elif operations[j] == 'D':
                table.append(int(table[-1])*2)
            elif operations[j] == 'C':
                del table[-1]
            else:
                table.append(int(operations[j]))
            j += 1
        return sum(table)

                