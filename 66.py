from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def add_one(index:int):
            if index<0:
                digits.insert(0,1)
                return
            digits[index] += 1
            if digits[index] == 10:
                digits[index] = 0
                add_one(index-1)
                return
        add_one(len(digits)-1)
        return digits



