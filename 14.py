from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        strs.sort()


        first = strs[0]
        last = strs[-1]
        minLength = min(len(first),len(last))

        for i in range(minLength):
            if first[i]!=last[i]:
                return first[:i]

        return first[:minLength]

Solution().longestCommonPrefix(["aaa","aa","aaa"])