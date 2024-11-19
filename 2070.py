from collections import defaultdict
from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        q_i_array = sorted([(q,i) for i,q in enumerate(queries)])

        res = [0]*len(queries)
        index=0
        maxB = 0
        for q,i in q_i_array:
            while index<len(items) and items[index][0]<=q:
                maxB = max(maxB,items[index][1])
                index+=1
            res[i] = maxB

        return res

Solution().maximumBeauty([[1,2],[3,2],[2,4],[5,6],[3,5]],[1,2,3,4,5,6])
