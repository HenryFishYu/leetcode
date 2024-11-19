class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        xIndex = 1
        nIndex = 1
        while nIndex <= n-1:
            if xIndex & x==0:
                if nIndex & (n-1):
                    res = res | xIndex
                nIndex = nIndex << 1
            xIndex = xIndex << 1

        return res

print(Solution().minEnd(3,4))
