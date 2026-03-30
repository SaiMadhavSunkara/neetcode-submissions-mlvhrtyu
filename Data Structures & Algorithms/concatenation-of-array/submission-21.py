class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        i, j  = 0, len(nums)-1
        while i <= j:
            nums.append(nums[i])
            i += 1
        return nums
            
