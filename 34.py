from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:


        def find_mid_index(left: bool):
            l,r = 0, len(nums)-1
            res = -1
            while l<=r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                    continue
                if nums[mid] > target:
                    r = mid - 1
                    continue
                if left:
                    res = mid
                    r = mid-1
                    continue
                if not left:
                    res = mid
                    l = mid + 1
                    continue
            return res
        l = find_mid_index(True)
        if l == -1:
            return [-1,-1]
        return [l,find_mid_index(False)]
