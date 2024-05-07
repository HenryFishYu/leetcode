from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tmp = [g - c for g,c in zip(gas, cost)]
        if sum(tmp)<0:
            return -1
        total = 0
        for i,v in enumerate(tmp):
            total += v
            if total<0:
                return i+1

Solution().canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2])