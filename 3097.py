from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res = float("inf")
        bits = [0]*32

        def set_bits(num:int,diff:int):
            for i in range(len(bits)):
                if num & 1 << i > 0:
                    bits[i] += diff

        def bits_to_int():
            intValue = 0
            for i in range(len(bits)):
                if bits[i]:
                    intValue |= 1 << i
            return intValue

        l=0
        for r in range(len(nums)):
            set_bits(nums[r],1)

            while l<=r and bits_to_int()>=k:
                res = min(res,r-l+1)
                set_bits(nums[l],-1)
                l+=1

        return res if res!=float("inf") else -1


Solution().minimumSubarrayLength([1,2,3],2)