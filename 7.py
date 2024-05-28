class Solution:
    def reverse(self, x: int) -> int:
        flg = 1
        if x<0:
            flg = -1
            x = -x
        res = 0
        while x:
            res = res*10+x%10
            x = x//10
        return flg*res