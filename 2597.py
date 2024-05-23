from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        res = 0
        temp = []
        nums.sort()
        def dfs(i: int):
            if i >= len(nums):
                return
            if temp:
                nonlocal res
                res += 1
            if temp and nums[i]-k in temp:
                print(1)
            else:
                dfs(i + 1)
                temp.append(nums[i])
                dfs(i + 1)
                temp.remove(nums[i])
        dfs(0)
        return res

print(Solution().beautifulSubsets([10,4,5,7,2,1],3))


