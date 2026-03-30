class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new_list = []
        nums.sort()
        n = len(nums)
        i = 0
        
        while i < n - 2:
            j = n - 1
            k = i + 1
            while k < j:
                total = nums[i] + nums[k] + nums[j]
                
                if total == 0:
                    if [nums[i], nums[k], nums[j]] not in new_list:
                        new_list.append([nums[i], nums[k], nums[j]])
                    k += 1
                    j -= 1
                elif total > 0:
                    j -= 1
                else:
                    k += 1
            i += 1
            
        return new_list