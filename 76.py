class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetMap = {}

        tempMap = {}
        tempCount = 0
        for c in t:
            targetMap[c] = 1 + targetMap.get(c,0)
        targetCount = len(targetMap)
        minLength = len(s)
        res = ""
        leftIndex = 0
        for i,v in enumerate(s):
            if v in targetMap:
                tempMap[v] = 1+ tempMap.get(v, 0)
                if tempMap[v] == targetMap[v]:
                    tempCount += 1

                while tempCount==targetCount:
                    if i-leftIndex < minLength:
                        minLength = i-leftIndex
                        res = s[leftIndex:i+1]

                    if s[leftIndex] in targetMap:
                        tempMap[s[leftIndex]] -= 1
                        if tempMap[s[leftIndex]] < targetMap[s[leftIndex]]:
                            tempCount -= 1
                    leftIndex += 1
        return res

print(Solution().minWindow("ADOBECODEBANC","ABC"))