class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        flag = 1
        if s[0] in "-+":
            if s[0] == '-':
                flag = -1
            s = s[1:]

        res = None
        for i in range(len(s)):
            if not s[i].isnumeric():
                res = s[:i]
                break
            if i == len(s)-1:
                res = s
        if not res:
            return 0
        res = flag*int(res)
        return max(-2**31,min(res,2**31-1))


print(Solution().myAtoi("-+12"))