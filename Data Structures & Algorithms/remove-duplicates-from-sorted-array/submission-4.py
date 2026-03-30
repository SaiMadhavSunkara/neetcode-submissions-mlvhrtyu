class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        temp = nums[0]
        while j < len(nums):
            if temp == nums[j]:
                j += 1
            elif temp < nums[j]:
                temp = nums[j]
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return i+1
        

