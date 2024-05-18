from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(current: str,total: int):
            if total>n or total<0 or len(current)>n*2:
                return
            if len(current) == n*2 and total==0:
                res.append(current)
                return

            backtrack(current+'(',total+1)
            backtrack(current+')',total-1)

        backtrack("",0)
        return res

print(Solution().generateParenthesis(3))