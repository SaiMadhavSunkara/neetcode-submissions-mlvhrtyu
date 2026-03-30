class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        storage = {}
        new_arr = []
        i, j = 0, len(nums)

        for _ in range(len(nums)):
            storage[_] = nums[i]

        for i in range(len(nums)):
            pdt = 1
            for j in range(len(nums)):
                if i != j:
                    pdt *= nums[j]
            new_arr.append(pdt)
        return new_arr


