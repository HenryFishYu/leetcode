class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        temp = divisor

        A = abs(dividend)
        B = abs(divisor)

        while A>=B:
            temp = B
            mul = 1
            while A>=temp:
                A-=temp
                res+=mul
                temp+=temp
                mul+=mul

        if (divisor<0 and dividend>0) or (divisor>0 and dividend<0):
            res = -res
        return max(-2**31,min(2**31-1,res))