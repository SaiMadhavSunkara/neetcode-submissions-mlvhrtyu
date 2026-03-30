class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        new_str = "" 
        if len(word1) < len(word2):
            j = len(word1)-1 
        else:
            j = len(word2)-1
        while i <= j:
            new_str += word1[i]
            new_str += word2[i]
            i += 1
        if len(word1) > len(word2):
            new_str += word1[i:]
        elif len(word2) > len(word1):
            new_str += word2[i:]
        return new_str
