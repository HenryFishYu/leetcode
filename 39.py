from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        candidates_length = len(candidates)
        res = []
        def backtrack(i: int,current_arr: list,total: int):
            if i >= candidates_length or total>target:
                return
            if total == target:
                res.append(current_arr.copy())
                return

            backtrack(i + 1, current_arr, total)
            num = candidates[i]
            current_arr.append(num)
            backtrack(i,current_arr,total+num)
            current_arr.pop()

        backtrack(0,[],0)
        return res


print(Solution().combinationSum([8,7,4,3],11))

