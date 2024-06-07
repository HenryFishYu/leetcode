from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        nums.sort()

        def helper(used:list):
            if len(used)==len(nums):
                res.append(temp.copy())
                return
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1] and i-1 in used:
                    continue
                if i in used:
                    continue
                temp.append(nums[i])
                used.append(i)
                helper(used)
                used.pop()
                temp.pop()

        helper([])
        return res

print(Solution().permuteUnique([1,1,2]))