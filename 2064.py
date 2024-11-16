import math



class Solution(object):
    def minimizedMaximum(self, n, quantities):
        def is_valid(number: int):
            required_n = 0
            for quantity in quantities:
                required_n += math.ceil(quantity / number)
            return required_n <= n

        l,r = 1,max(quantities)
        res = 0
        while l<=r:
            mid = (l+r)//2
            if is_valid(mid):
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res

print(Solution().minimizedMaximum(7,[15,10,10]))

