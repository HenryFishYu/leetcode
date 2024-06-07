from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left,right = 0,n-1
        up,bottom = 0,n-1

        res = [[0 for _ in range(n)] for _ in range(n)]

        count = 1
        while left<=right and up<=bottom:
            for i in range(left,right+1):
                res[up][i] = count
                count+=1

            up += 1

            for i in range(up,bottom+1):
                res[i][right] = count
                count+=1

            right -=1

            if not left<=right and not up<=bottom:
                return res

            for i in range(right,left-1,-1):
                res[bottom][i] = count
                count += 1

            bottom -=1

            for i in range(bottom,up-1,-1):
                res[i][left] = count
                count += 1

            left += 1
        return res

print(Solution().generateMatrix(5))



