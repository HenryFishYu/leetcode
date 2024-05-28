from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        difference = float("inf")
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l<r:
                temp = nums[l]+nums[i]+nums[r]
                if temp==target:
                    return target
                if temp<target:
                    l = l+1
                else:
                    r = r-1
                if abs(temp-target)<difference:
                    difference = abs(temp-target)
                    res = temp
        return res

print(Solution().threeSumClosest([4,0,5,-5,3,3,0,-4,-5],-2))