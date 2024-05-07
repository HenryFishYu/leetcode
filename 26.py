from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        number_of_unique = 0
        current_num = -1
        for num in nums:
            if num != current_num:
                current_num = num
                nums[number_of_unique] = current_num
                number_of_unique += 1
        return number_of_unique