from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftIndex = 0
        rightIndex = len(height)-1

        res = 0

        while leftIndex<rightIndex:
            res = max(res, (rightIndex - leftIndex) * min(height[leftIndex], height[rightIndex]))
            if height[leftIndex]<height[rightIndex]:
                leftIndex += 1
            else:
                rightIndex -= 1

        return res
