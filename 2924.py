from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = [0] * n

        for src,dest in edges:
            incoming[dest] += 1

        champions = []
        for i,value in enumerate(incoming):
            if not value:
                champions.append(i)

        if len(champions)==1:
            return champions[0]

        return -1

