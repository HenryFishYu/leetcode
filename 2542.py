import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1,n2) for n1,n2 in zip(nums1,nums2)]
        pairs.sort(key=lambda p:p[1],reverse=True)
        res = 0
        heap = []
        n1Sum = 0

        for n1,n2 in pairs:
            n1Sum += n1
            heapq.heappush(heap,n1)
            if len(heap)>k:
                n1Sum -= heapq.heappop(heap)
            if len(heap)==k:
                res = max(res,n1Sum*n2)

        return res

print(Solution().maxScore([1,3,3,2],[2,1,3,4],3))