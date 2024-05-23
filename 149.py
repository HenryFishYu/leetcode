from collections import defaultdict
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 1
        for i in range(len(points)):
            p1 = points[i]
            map = defaultdict(int)
            for k in range(i+1,len(points)):
                p2 = points[k]
                if p1[0] == p2[0]:
                    val = float("inf")
                else:
                    val = (p1[1]-p2[1])/(p1[0]-p2[0])

                map[val] += 1
                res = max(res,map[val]+1)
        return res


print(Solution().maxPoints([[1,1],[2,2],[3,3]]))