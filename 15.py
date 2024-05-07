from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)

        res = set()
        for i1 in range(length-2):
            v1 = nums[i1]
            i2 = i1+1
            i3 = length-1
            while i2<i3:
                v2 = nums[i2]
                v3 = nums[i3]
                if v1+v2+v3 == 0:
                    res.add((v1,v2,v3))
                    i2 += 1
                    i3 -= 1
                    continue
                if v1 + v2 + v3 > 0:
                    i3 -=1
                    continue
                if v1 + v2 + v3 < 0:
                    i2 +=1
                    continue
        return res


print(Solution().threeSum([-1,0,1,2,-1,-4]))