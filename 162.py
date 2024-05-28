from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l<r:
            mid = (l+r)//2
            mid_value = nums[mid]

            if nums[mid - 1] < mid_value >   nums[mid + 1]:
                return mid
            if mid_value>nums[mid+1]:
                r = mid
            else:
                l = mid+1
        return l
