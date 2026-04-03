class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        ana = []

        for i in strs:
            count = [0] * 26

            for c in i:
                count [ord(c) - ord('a')] += 1

            key = tuple(count)
            if not key in hashmap:
                hashmap[key] = [i]
            else:
                hashmap[key].append(i)
        for i in hashmap:
            ana.append(hashmap[i])
        return ana

    







