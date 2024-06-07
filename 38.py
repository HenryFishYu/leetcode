class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        prev = self.countAndSay(n-1)
        current = prev[0]
        count = 1
        res = ""
        for c in prev[1:]:
            if c==current:
                count+=1
            else:
                res+=str(count)+str(current)
                current = c
                count = 1
        res+=str(count)+str(current)
        return res

print(Solution().countAndSay(4))
