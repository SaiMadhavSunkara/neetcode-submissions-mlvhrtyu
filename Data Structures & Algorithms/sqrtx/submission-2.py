class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while low <= high:
            mid = int((low + high)/2)
            if x < mid*mid:
                high = mid - 1
            elif x > mid*mid:
                low = mid + 1
                res = mid
            else:
                return mid
        return res
            