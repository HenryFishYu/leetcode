class Solution:
    def __init__(self):
        self.dp = {}
    def isMatch(self, s: str, p: str) -> bool:
        if (s,p) in self.dp:
            return self.dp[(s,p)]
        if not s and not p:
            self.dp[(s, p)] = True
            return True
        if not p:
            self.dp[(s, p)] = False
            return False
        first = p[0]
        if not s and first!='*':
            self.dp[(s, p)] = False
            return False

        if first == '*':
            if not s:
                self.dp[(s, p)] = self.isMatch(s,p[1:])
                return self.dp[(s, p)]
            self.dp[(s, p)] = self.isMatch(s[1:],p[1:]) or self.isMatch(s[1:],p) or self.isMatch(s,p[1:])
            return self.dp[(s, p)]

        if first == '?' or first == s[0]:
            self.dp[(s, p)] = self.isMatch(s[1:],p[1:])
            return self.dp[(s, p)]
        self.dp[(s, p)] = False
        return self.dp[(s, p)]

print(Solution().isMatch("adceb","*a*b"))