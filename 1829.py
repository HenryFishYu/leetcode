import math
from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        maxK = (1 << maximumBit) -1
        res = [maxK]

        for num in nums:
            res.append(num ^ res[-1])

        res = res[1:]
        res.reverse()
        return res


Solution().getMaximumXor([0,1,1,3],2)


