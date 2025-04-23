import math
from collections import defaultdict
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        map = defaultdict(int)

        for answer in answers:
            map[answer] = map[answer]+1

        res = 0

        for k,v in map.items():
            res += math.ceil(v/(k+1))*(k+1)
        return res


print(Solution().numRabbits([1,0,1,0,0]))