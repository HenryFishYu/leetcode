from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums.copy()]

        res = []

        for i in range(len(nums)):
            first = nums.pop(0)
            temp_res = self.permute(nums)
            for temp in temp_res:
                temp.append(first)
            nums.append(first)
            res.extend(temp_res)
        return res

print(Solution().permute([1,2,3]))
