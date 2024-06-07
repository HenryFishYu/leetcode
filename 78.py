from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []

        def dfs(i):
            if i==len(nums):
                res.append(temp.copy())
                return
            dfs(i+1)
            temp.append(nums[i])
            dfs(i+1)
            temp.pop()

        dfs(0)
        return res

print(Solution().subsets([1,2,3]))




