class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in hashset:
                return [hashset[diff], index]
            hashset[num] = index
        return 

                