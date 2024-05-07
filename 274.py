from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        count_citations = [0 for _ in range(length+1)]

        for v in citations:
            if v>=length:
                count_citations[length] +=1
            else:
                count_citations[v] += 1

        total = 0
        for i in range(length,-1,-1):
            total += count_citations[i]
            if count_citations[i]<= total:
                return i
        return 0

Solution().hIndex([3,0,6,1,5])