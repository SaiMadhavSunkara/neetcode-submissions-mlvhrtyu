class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = {}
        for i in nums:
            if i not in majority:
                majority[i] = 0
            else:
                majority[i] += 1

        return max(majority, key=majority.get)