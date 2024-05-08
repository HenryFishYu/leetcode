class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        used = set()
        map = {}
        for i in range(len(s)):
            if s[i] not in map:
                if t[i] in used:
                    return False
                map[s[i]] = t[i]
                used.add(t[i])
                continue

            if map[s[i]] != t[i]:
                return False
        return True