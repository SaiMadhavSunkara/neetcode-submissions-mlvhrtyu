class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = nums[0]
        for i in nums:
            if res == i:
                count += 1
            elif count == 0:
                res = i
            else:
                count -= 1
        return res

            
            


        