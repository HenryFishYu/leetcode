from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for index,temperature in enumerate(temperatures):
            while stack and temperature>stack[-1][0]:
                _,i = stack.pop()
                res[i]=index-i
            stack.append((temperature,index))

        return res

