from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        map = {}
        for i,v in enumerate(nums):
            value = map.get(v-i,[v,-1])
            value[1] += 1
            map[v-i] = value

        res = []
        for k,v in map.items():
            if v[1] == 0:
                res.append(str(v[0]))
            else:
                res.append("{}->{}".format(v[0],v[0]+v[1]))
        return res

print(Solution().summaryRanges([0,1,2,4,5,7]))
