class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineMap = {}
        for c in magazine:
            magazineMap[c] = 1 + magazineMap.get(c,0)

        for c in ransomNote:
            if c not in magazineMap or magazineMap[c]<=0:
                return False
            magazineMap[c] -= 1
        return True