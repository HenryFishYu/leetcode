import heapq
from typing import List



class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        min_heap = [(c,p) for c,p in zip(capital,profits)]
        heapq.heapify(min_heap)
        for _ in range(k):
            while min_heap and min_heap[0][0]<=w:
                c,p = heapq.heappop(min_heap)
                heapq.heappush(heap,-p)
            if not heap:
                return w
            w += -heapq.heappop(heap)
        return w

print(Solution().findMaximizedCapital(2,0,[1,2,3],[0,1,1]))