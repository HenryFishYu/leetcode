from collections import defaultdict
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        dict = defaultdict(bool)
        max = 0
        for item in nums:
            dict[item] = True
            if (abs(item)>max) & (-item in dict):
                max = abs(item)
        return max
