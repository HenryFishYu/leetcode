from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        map = {}
        res = 0
        for i in range(len(nums)):
            v = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j]==v and i * j % k == 0:
                    res += 1

        return res


print(Solution().countPairs([3,1,2,2,2,1,3],2))
