class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        new_list = []
        n = len(nums)
        i = 0
        
        while i < n - 2:
            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            
            j = n - 1
            k = i + 1
            while k < j:
                total = nums[i] + nums[k] + nums[j]
                
                if total == 0:
                    new_list.append([nums[i], nums[k], nums[j]])
                    k += 1
                    j -= 1
                    # Skip duplicates for k
                    while k < j and nums[k] == nums[k-1]:
                        k += 1
                    # Skip duplicates for j
                    while k < j and nums[j] == nums[j+1]:
                        j -= 1
                elif total > 0:
                    j -= 1
                else:
                    k += 1
            i += 1
            
        return new_list