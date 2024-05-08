class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedS = [c for c in s]
        sortedS.sort()
        sortedT = [c for c in t]
        sortedT.sort()
        return sortedS == sortedT