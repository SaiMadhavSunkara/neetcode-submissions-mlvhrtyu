class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][-1] < target:
                continue
            elif matrix[i][-1] == target:
                return True
            else:
                low, high = 0, len(matrix[i]) - 1
                while low <= high:
                    mid = (low+high) // 2
                    if target == matrix[i][mid]:
                        return True
                    elif target > matrix[i][mid]:
                        low = mid + 1
                    else:
                        high = mid - 1
        return False





