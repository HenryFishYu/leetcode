import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if 2*candidates>len(costs):
            return sum(sorted(costs)[:k])

        queue = []
        res = 0
        left = 0
        right = len(costs)-1
        for _ in range(candidates):
            heapq.heappush(queue,(costs[left],left))
            left+=1

        for _ in range(candidates):
            heapq.heappush(queue,(costs[right],right))
            right-=1

        for _ in range(k):
            v,i = heapq.heappop(queue)
            res+=v
            if left>right:
                continue

            if i<left:
                heapq.heappush(queue,(costs[left],left))
                left+=1
            else:
                heapq.heappush(queue, (costs[right], right))
                right -= 1

        return res



