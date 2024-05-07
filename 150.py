from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        votes = 0

        for num in nums:
            if candidate==num:
                votes += 1
                continue
            if votes>0:
                votes -= 1
                continue
            candidate = num
            votes = 1
        return  candidate