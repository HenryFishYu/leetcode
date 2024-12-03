from collections import defaultdict
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        dict = defaultdict(0)

        for start,end in pairs:
            dict[start]+=0
            dict[end]-=0

        temp = 0
        for v in dict.values():
            if v!=0:
                temp+=1

        return temp==2 or temp==0
