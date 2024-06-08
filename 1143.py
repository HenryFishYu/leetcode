class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        dp[(0,0)] = 1 if text1[0]==text2[0] else 0
        def helper(i1,i2):
            if i1<0 or i2<0:
                return 0
            if (i1,i2) in dp:
                return dp[(i1,i2)]
            if text1[i1]==text2[i2]:
                dp[(i1, i2)] = helper(i1-1,i2-1)+1
            else:
                dp[(i1, i2)] = max(helper(i1,i2-1),helper(i1-1,i2))
            return dp[(i1,i2)]
        res = helper(len(text1)-1,len(text2)-1)
        return res


print(Solution().longestCommonSubsequence("bsbininm","jmjkbkjkv"))

