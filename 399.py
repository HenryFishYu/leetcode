from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        map=defaultdict(dict)
        visited = set()
        for i,v in enumerate(values):
            map[equations[i][0]][equations[i][1]] = v
            map[equations[i][1]][equations[i][0]] = 1/v

        def dfs(src, dest, res):
            if src not in map or dest not in map or src in visited:
                return -1
            if src == dest:
                return res
            visited.add(src)
            for middle,val in map[src].items():
                temp = dfs(middle,dest,val*res)
                if temp != -1:
                    return temp
            return -1

        res = []
        for query in queries:
            res.append(dfs(query[0],query[1],1))
        return res




