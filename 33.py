from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid

            if nums[l]>nums[mid] and target>nums[mid]:
                if target>=nums[l]:
                    r = mid-1
                else:
                    l = mid+1
                continue
            if nums[l] > nums[mid] and target < nums[mid]:
                r = mid-1
                continue

            if nums[l] <= nums[mid] and target > nums[mid]:
                l = mid+1
                continue
            if nums[l] <= nums[mid] and target < nums[mid]:
                if target < nums[l]:
                    l = mid+1
                else:
                    r = mid-1
                continue
        return -1

print(Solution().search([5,1,3],5))


