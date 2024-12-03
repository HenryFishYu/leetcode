from collections import defaultdict
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        map = defaultdict(int)

        for row in matrix:
            if row[0]:
                key = tuple([c^1 for c in row])
            else:
                key = tuple(row)
            map[key] += 1

        return max(map.values())

