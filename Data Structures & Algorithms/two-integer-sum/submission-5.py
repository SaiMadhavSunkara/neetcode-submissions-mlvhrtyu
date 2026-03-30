class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i in range(len(nums)):
            hash[nums[i]] = i

        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in hash and hash[temp] != i:
                low = min(hash[temp], i)
                high = max(hash[temp], i)
                return [low, high]