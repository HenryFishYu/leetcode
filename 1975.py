from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        flatten = [column for row in matrix for column in row]

        number_of_negatives = 0
        for num in flatten:
            if num <0:
                number_of_negatives += 1

        res = sum([abs(num) for num in flatten])
        min_abs = min([abs(num) for num in flatten])
        if min_abs==0:
            return res

        if number_of_negatives%2==1:
            res -= 2*min_abs
        return res


Solution().maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]])