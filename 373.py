import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        res = []
        for index1 in range(min(len(nums1),k)):
                heapq.heappush(heap, (nums1[index1] + nums2[0], index1, 0))

        for _ in range(k):
            _, i1, i2 = heapq.heappop(heap)
            res.append([nums1[i1], nums2[i2]])
            if i2+1 < len(nums2):
                heapq.heappush(heap,(nums1[i1]+nums2[i2+1],i1,i2+1))
        return res