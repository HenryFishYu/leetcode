from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        number_of_unique = 0
        current_num = None
        count_of_unique = 0
        for num in nums:
            if (num == current_num) & (count_of_unique>=2):
                continue
            if num != current_num:
                current_num = num
                nums[number_of_unique] = current_num
                number_of_unique += 1
                count_of_unique = 1
                continue
            count_of_unique += 1
            nums[number_of_unique] = current_num
            number_of_unique += 1
        return number_of_unique

print(Solution().removeDuplicates([1,1,1,2,2,3]))