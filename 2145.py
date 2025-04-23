from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        max_number = 0
        min_number = 0

        current = 0
        for difference in differences:
            current += difference
            if difference>0:
                max_number = max(max_number,current)
            else:
                min_number = min(min_number,current)

        return max(0,upper-lower+1-(max_number-min_number))
