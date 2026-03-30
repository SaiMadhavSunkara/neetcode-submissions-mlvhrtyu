class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, k
        for i in range(k):
            res = nums.pop()
            nums.insert(0, res)
        
        