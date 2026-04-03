class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        ana = []

        for i in range(len(strs)):
            sortedstr = ''.join(sorted(strs[i]))
            if not sortedstr in hashmap:
                temp = []
                temp.append(strs[i])
                hashmap[sortedstr] = temp
            else:
                temp = hashmap[sortedstr]
                temp.append(strs[i])
                hashmap[sortedstr] = temp
        for i in hashmap:
            ana.append(hashmap[i])
        return ana

    







