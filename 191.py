class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            if n & 1 > 0:
                res += 1
            n = n>>1
        return res
print(Solution().hammingWeight(3))