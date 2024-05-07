class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        hitNoneSpace = False
        res = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':
                hitNoneSpace = True
                res += 1
                continue
            if (s[i] == ' ') & hitNoneSpace:
                break
        return res