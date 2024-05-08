class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        map = {'}':'{',')':'(',']':'['}

        for c in s:
            if stack and c in map:
                if map[c]==stack[-1]:
                    stack.pop()
                    continue
                return False
            else:
                stack.append(c)
        return True if not stack else False
