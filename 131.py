class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        temp = []

        def isPar(s:str):
            l,r = 0,len(s)-1
            while l<r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i:int):
            if i>=len(s):
                res.append(temp.copy())
                return
            for r in range(i,len(s)):
                element = s[i:r+1]
                if isPar(element):
                    temp.append(element)
                    dfs(r+1)
                    temp.pop()
        dfs(0)
        return res