from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if nums[0]<nums[-1]:
            return nums[0]
        nums.insert(0,float("inf"))
        nums.append(float("inf"))
        l, r = 1, len(nums)-2
        while l<=r:
            mid = (l+r)//2
            if nums[mid-1]>nums[mid]<nums[mid+1]:
                return nums[mid]
            if nums[mid]>=nums[1]:
                l = mid+1
                continue
            if nums[mid]<nums[1]:
                r = mid-1
                continue
        return 0

print(Solution().findMin([4,5,6,1,2,3]))