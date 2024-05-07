class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            index = t.find(c)
            if index == -1:
                return False
            t = t[index+1:]
        return True

Solution().isSubsequence("axc","ahbgdc")