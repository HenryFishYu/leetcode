from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        def backtrace(start_index: int,comb: list):
            if len(comb)== k:
                res.append(comb.copy())
                return
            for i in range(start_index,n+1):
                comb.append(i)
                backtrace(i+1,comb)
                comb.pop()

        backtrace(1,[])
        return res

print(Solution().combine(4,2))