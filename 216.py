from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        temp = []
        def backtrack(number:int):
            if sum(temp)==n and len(temp)==k:
                res.append(temp.copy())
                return
            if number>9:
                return

            backtrack(number+1)
            temp.append(number)
            backtrack(number + 1)
            temp.pop()

        backtrack(1)
        return res

print(Solution().combinationSum3(3,9))



