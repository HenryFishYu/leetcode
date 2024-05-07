import re
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words.sort()
        targetLength = len(words[0])*len(words)

        res = []
        for i in range(0,len(s)-targetLength+1):
            tempStr = s[i:i+targetLength]
            tempStrArr = re.findall('.'*len(words[0]),tempStr)
            tempStrArr.sort()
            if tempStrArr==words:
                res.append(i)

        return res

print(Solution().findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"]))