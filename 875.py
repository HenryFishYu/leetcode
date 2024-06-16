import bisect
from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h==len(piles):
            return max(piles)

        def count(mid_value: int):
            mid_index = bisect.bisect_left(piles,mid_value)-1
            res = mid_index+1
            for e in piles[mid_index+1:]:
                res += ceil(e/mid_value)
            return res

        piles.sort()
        min_v = 1
        max_v = piles[-1]
        res = max_v
        mid = (min_v + max_v) // 2
        while min_v<=max_v:
            count_mid = count(mid)
            if count_mid>h:
                min_v = mid+1
            else:
                max_v = mid-1
                res = min(res,mid)
            mid = (min_v + max_v) //2
        return res

print(Solution().minEatingSpeed([3,6,7,11],8))