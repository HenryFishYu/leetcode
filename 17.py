from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        def backtrack(combination, digits):
            nonlocal res
            if len(digits) == 0:
                res.append(combination)
                return

            c = digits[0]
            for charactor in phone_map[c]:
                backtrack(combination+charactor,digits[1:])

        backtrack("",digits)
        return res
