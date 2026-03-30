class Solution:
    def calPoints(self, operations: List[str]) -> int:
        new_list = []
        temp = 0
        for i in operations:
            if i == 'C':
                new_list.pop()
            elif i == 'D':
                temp = new_list[-1] * 2
                new_list.append(temp)
            elif i == '+':
                new_list.append(new_list[-1] + new_list[-2])
            else:
                new_list.append(int(i))
        temp = 0
        for i in new_list:
            temp += i
        return temp
