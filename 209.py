from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        leftIndex = 0
        rightIndex = 0

        tmpSum = nums[0]
        res = 999999
        while rightIndex<len(nums):

            if tmpSum >= target:
                res = min(res,rightIndex-leftIndex+1)
                tmpSum -= nums[leftIndex]
                leftIndex += 1
                continue

            rightIndex += 1
            if rightIndex<len(nums):
                tmpSum += nums[rightIndex]
        return res

