from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        tmp = [1] * len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                tmp[i] = tmp[i-1] + 1

        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                tmp[i] = max(tmp[i],tmp[i+1]+1)

        return sum(tmp)
Solution().candy([1,3,2,2,1])