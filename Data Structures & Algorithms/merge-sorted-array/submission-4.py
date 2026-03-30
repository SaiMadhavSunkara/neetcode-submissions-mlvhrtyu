class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        k = 0
        while k < n:
            if nums1[i] <= nums2[k] and i < m:
                    i += 1
            else:
                nums1.pop()
                nums1.insert(i, nums2[k])
                k += 1
                i += 1
                m += 1
            
            

