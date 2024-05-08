from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        map = {}
        res = 0
        for num in nums:
            left_count = map.get(num-1,0)
            right_count = map.get(num+1,0)
            count = left_count+right_count+1
            map[num] = count
            map[num-left_count] = count
            map[num+right_count] = count
            res = max(res,count)
        return res