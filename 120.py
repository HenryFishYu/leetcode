from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]

        for i in range(len(triangle)-2,-1,-1):
            for k in range(len(triangle[i])):
                triangle[i][k] += min(triangle[i+1][k],triangle[i+1][k+1])

        return triangle[0][0]
