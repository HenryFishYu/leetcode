from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s_pointer = 0
        spaces_pointer = 0

        res = []

        while s_pointer<len(s) and spaces_pointer<len(spaces):
            if s_pointer<spaces[spaces_pointer]:
                res.append(s[s_pointer])
                s_pointer += 1
            else:
                res.append(" ")
                spaces_pointer += 1

        res.append(s[s_pointer:])

        return "".join(res)

Solution().addSpaces("LeetcodeHelpsMeLearn",[8,13,15])