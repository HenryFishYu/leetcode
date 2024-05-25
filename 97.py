from collections import defaultdict


class Solution:
    def __init__(self):
        self.cache_map = {}
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2 and not s3:
            return True

        if (s1,s2,s3) in self.cache_map:
            return self.cache_map[(s1,s2,s3)]

        res1, res2 = False, False
        if s1 and s3 and s1[0] == s3[0]:
            res1 = self.isInterleave(s1[1:],s2,s3[1:])

        if s2 and s3 and s2[0] == s3[0]:
            res2 = self.isInterleave(s1,s2[1:],s3[1:])
        self.cache_map[(s1,s2,s3)] = res1 or res2

        return res1 or res2

print(Solution().isInterleave("aabcc","dbbca","aadbbcbcac"))

