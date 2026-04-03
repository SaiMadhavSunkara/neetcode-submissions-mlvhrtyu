class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        ana = []

        for i in strs:
            count = 0
            for c in i:
                count += ord(c)
            if not count in hashmap:
                temp = []
                temp.append(i)
                hashmap[count] = temp
            else:
                hashmap[count].append(i)
        for i in hashmap:
            ana.append(hashmap[i])
        return ana

    







