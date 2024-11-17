from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        def binary_search(leftIndex:int,target):
            l,r = leftIndex,len(nums)-1

            while l<=r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
            return r


        res = 0
        for i in range(len(nums)):
            res += binary_search(i+1,upper+1-nums[i])-binary_search(i+1,lower-nums[i])
        return res


print(Solution().countFairPairs([0,1,7,4,4,5],3,6))