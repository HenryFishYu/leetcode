class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)

        res = [[float("inf")]*(len2+1) for _ in range(len1+1)]

        for i in range(len1+1):
            res[i][len2] = len1-i

        for i in range(len2+1):
            res[len1][i] = len2-i

        for i1 in range(len1-1,-1,-1):
            for i2 in range(len2-1,-1,-1):
                if word1[i1] == word2[i2]:
                    res[i1][i2] = res[i1+1][i2+1]
                else:
                    res[i1][i2] = 1 + min(res[i1+1][i2],res[i1][i2+1],res[i1+1][i2+1])

        return res[0][0]

print(Solution().minDistance("horse","ros"))