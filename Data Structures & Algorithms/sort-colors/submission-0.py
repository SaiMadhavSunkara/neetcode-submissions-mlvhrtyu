class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0 
        bucket = {
            0: 0,
            1: 0,
            2: 0
        }
        for i in range(len(nums)):
            bucket[nums[i]] += 1
        for i in bucket:
            for _ in range(bucket[i]):
                nums[l] = i
                l += 1



            
            

            
        

        