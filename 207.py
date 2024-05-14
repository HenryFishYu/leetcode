from array import array
from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map = defaultdict(list)
        for prerequisity in prerequisites:
            map[prerequisity[0]].append(prerequisity[1])

        visited_set = set()
        def dfs(current):
            if current in visited_set:
                return False
            if len(map[current])==0:
                return True

            visited_set.add(current)
            for item in map[current]:
                if not dfs(item):
                    return False
            visited_set.remove(current)
            map[current] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True



Solution().canFinish(3,[[0,1],[0,2],[1,2]])
