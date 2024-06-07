from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prev = intervals[0]
        for interval in intervals[1:]:
            if prev[1]>interval[0]:
                res+=1
            else:
                prev = interval
        return res
