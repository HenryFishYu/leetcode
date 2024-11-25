from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = 0
        mask = 1
        for i in range(32):
            tempMax = 0
            for candidate in candidates:
                if candidate & mask:
                    tempMax += 1
            res = max(res,tempMax)
            mask = mask << 1

        return res
