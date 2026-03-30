class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}
        new_temp = []

        for i in range(len(strs)):
            temp = []
            k = ''.join(sorted(strs[i]))
            if k in anag:
                temp = anag[k]
                temp.append(strs[i])
                anag[k] = temp
            else:
                temp.append(strs[i])
                anag[k] = temp
        return list(anag.values())



