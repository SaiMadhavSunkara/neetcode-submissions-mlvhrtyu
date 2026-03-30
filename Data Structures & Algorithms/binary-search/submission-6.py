class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid+1 
            else:
                high = mid 
        return -1