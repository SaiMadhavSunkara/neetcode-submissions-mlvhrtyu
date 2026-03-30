class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j, k = 0, len(s) - 1, 1
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif k > 0:
                left_skip_i, left_skip_j = i + 1, j
                right_skip_i, right_skip_j = i, j - 1
                def check(l, r):
                    while l < r:
                        if s[l] != s[r]:
                            return False
                        l += 1
                        r -= 1
                    return True
                if check(left_skip_i, left_skip_j) or check(right_skip_i, right_skip_j):
                    return True
                return False
            else:
                return False
        return True