from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res,temp = [],[]

        def k_sum(k,start,target):
            if k>2:
                for i in range(start,len(nums)-k+1):
                    if i>start and nums[i]==nums[i-1]:
                        continue
                    temp.append(nums[i])
                    k_sum(k-1,i+1,target-nums[i])
                    temp.pop()

            else:
                l,r = start,len(nums)-1
                while l<r:
                    if nums[l]+nums[r]>target:
                        r = r-1
                        continue
                    if nums[l] + nums[r] < target:
                        l = l +1
                        continue
                    if nums[l] + nums[r] == target:
                        res.append(temp+[nums[l],nums[r]])
                        l += 1
                        while l<r and nums[l-1]==nums[l]:
                            l +=1

        k_sum(4,0,target)
        return res



