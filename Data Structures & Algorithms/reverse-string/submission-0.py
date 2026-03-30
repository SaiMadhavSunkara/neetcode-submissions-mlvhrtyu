class Solution:
    def reverseString(self, s: List[str]) -> None: 
        k = 0
        j = len(s) - 1
        bound = int(len(s)/2)

        while k < j:
            s[k] , s[j] = s[j], s[k]
            j -= 1
            k += 1

            

        """
        Do not return anything, modify s in-place instead.
        """
        