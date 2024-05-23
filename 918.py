from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_min, global_max = nums[0], nums[0]
        cur_min, cur_max = 0, 0
        total = 0

        for num in nums:
            cur_min = min(cur_min+num, num)
            cur_max = max(cur_max+num, num)
            global_min = min(global_min,cur_min)
            global_max = max(global_max, cur_max)
            total+=num

        return global_max

print(Solution().maxSubarraySumCircular([1,-2,3,-2]))