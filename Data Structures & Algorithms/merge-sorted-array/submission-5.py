class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        k = 0
        while i < m and k < n:
            if nums1[i] > nums2[k]:
                nums1.insert(i, nums2[k])
                nums1.pop()
                k += 1
                m += 1  
            i += 1

        while k < n:
            nums1[m] = nums2[k]
            m += 1
            k += 1

            
            

