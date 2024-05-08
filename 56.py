from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0],x[1]))
        res = [intervals[0]]
        for v in intervals[1:]:
            if res[-1][1]<v[0]:
                res.append(v)
            else:
                res[-1][1] = max(res[-1][1],v[1])
        return res


