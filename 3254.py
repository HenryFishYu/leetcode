from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = 1
        l = 0
        for r in range(len(nums)):
            if r >0 and nums[r] == nums[r-1]+1:
                count += 1

            if r-l+1>k:
                if nums[l]+1==nums[l+1]:
                    count -=1
                l+=1

            if r-l+1==k:
                if count==k:
                    res.append(nums[r])
                else:
                    res.append(-1)

        return res

print(Solution().resultsArray([3,2,3,2,3,2],2))

