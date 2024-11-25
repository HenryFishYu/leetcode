from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        current_min, current_max, current_bits = nums[0], nums[0], bin(nums[0]).count("1")
        previous_max = 0

        for num in nums:
            if bin(num).count("1") == current_bits:
                current_min = min(current_min, num)
                current_max = max(current_max, num)
                continue

            if current_min < previous_max:
                return False

            previous_max = current_max
            current_min = num
            current_max = num
            current_bits = bin(num).count("1")

        if current_min < previous_max:
            return False

        return True
