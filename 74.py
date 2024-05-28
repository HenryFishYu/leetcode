from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        def num_to_value(num: int):
            r = num // COLS
            c = num % COLS
            return matrix[r][c]

        l = 0
        r = ROWS*COLS-1
        if l == r:
            return num_to_value(l)==target
        while l <= r:
            middle = (l + r) // 2
            middle_value = num_to_value(middle)
            if target==middle_value:
                return True
            if target> middle_value:
                l = middle+1
                continue
            if target < middle_value:
                r = middle-1
                continue
        return False

print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))

