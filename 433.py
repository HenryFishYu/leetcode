from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        def difference(s1: str,s2: str):
            res = 0
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    res+=1
            return res


        map = {k:False for k in bank}

        queue = deque()

        queue.append((0,startGene))

        while queue:
            times, current = queue.popleft()
            if current==endGene:
                return times

            temp = []
            for temp_str in bank:
                if difference(current,temp_str)==1:
                    queue.append((times+1,temp_str))
                else:
                    temp.append(temp_str)
            bank = temp
        return -1

print(Solution().minMutation("AACCGGTT","AAACGGTA",["AACCGGTA","AACCGCTA","AAACGGTA"]))
