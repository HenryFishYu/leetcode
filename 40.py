from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        candidates.sort()

        def solve(start,target):
            if target==0:
                res.append(temp.copy())
            if target<0:
                return
            if start == len(candidates):
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                temp.append(candidates[i])
                solve(i+1,target-candidates[i])
                temp.pop()

        solve(0,target)
        return res

print(Solution().combinationSum2([10,1,2,7,6,1,5],8))