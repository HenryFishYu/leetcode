from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        map = {}
        end = []
        res = []
        for e in arr2:
            map[e]=0

        for e in arr1:
            if e in map:
                map[e]+=1
            else:
                end.append(e)

        for e in arr2:
            for _ in range(map[e]):
                res.append(e)

        return res+sorted(end)
