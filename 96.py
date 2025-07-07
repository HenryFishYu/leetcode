import datetime
import time


class Solution:
    def numTrees(self, n: int) -> int:
        cache = {}
        def helper(start,end)->int:
            if start==end:
                return 1
            if start>end:
                return 1
            if (start,end) in cache:
                return cache[(start,end)]
            res = 0
            for i in range(start,end+1):
                res += helper(start,i-1)*helper(i+1,end)
            cache[(start,end)] = res
            return res
        return helper(1,n)

startTime = time.time()
print(Solution().numTrees(400))
print(time.time()-startTime)