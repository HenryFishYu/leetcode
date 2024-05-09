class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(i):
            res,digit,sign = 0,0,1
            while i< len(s):
                c = s[i]
                if c.isnumeric():
                    digit = digit*10+int(c)
                    i += 1
                    continue
                if c=='+':
                    res += (digit*sign)
                    digit = 0
                    sign = 1
                    i += 1
                    continue
                if c=='-':
                    res += (digit*sign)
                    digit = 0
                    sign = -1
                    i += 1
                    continue
                if c=='(':
                    sub_res,i = evaluate(i+1)
                    res += sub_res * sign
                    i+=1
                    continue
                if c==')':
                    res += digit * sign
                    return res,i
            return res + digit*sign

        return evaluate(0)