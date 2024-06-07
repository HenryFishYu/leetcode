from collections import defaultdict
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        defaultdict
        if not numRows:
            return []
        res = [[1]]
        for i in range(1,numRows):
            temp = []
            for t in range(i+1):
                if t==0:
                    temp.append(res[i-1][t])
                    continue
                if t==i:
                    temp.append(res[i - 1][t-1])
                    continue
                temp.append(res[i-1][t-1]+res[i-1][t])
            res.append(temp)
        return res

print(Solution().generate(3))
