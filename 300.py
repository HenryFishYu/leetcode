import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subseq = []
        for num in nums:
            index = bisect.bisect_left(subseq,num)
            if index >= len(subseq):
                subseq.append(num)
            else:
                subseq[index] = num
        return len(subseq)