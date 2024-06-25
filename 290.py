class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map = {}
        used = set()
        s_pattern = s.split()
        if len(pattern)!=len(s_pattern):
            return False

        for i,v in enumerate(pattern):
            if v in map:
                if s_pattern[i]!=map[v]:
                    return False
                else:
                    continue
            if s_pattern[i] in used:
                return False
            map[v] = s_pattern[i]
            used.add(s_pattern[i])

        return True

print(Solution().wordPattern("abc","dog cat dog"))
