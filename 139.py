from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[-1] = True
        for i in range(len(dp)-1,-1,-1):
            for word in wordDict:
                if i+len(word)<len(dp) and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]

        return dp[0]

print(Solution().wordBreak("catsandog",["cats","dog","sand","and","cat"]))
