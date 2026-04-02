class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        new_str = ""
        for i in range(len(strs[0])):
            for _ in strs:
                if i == len(_) or _[i] != strs[0][i]:
                    return new_str
            new_str += strs[0][i]
        return new_str
            
            







                

            