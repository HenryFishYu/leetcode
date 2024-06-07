class Solution:
    def longestValidParentheses(self, s: str) -> int:
        heap = []
        dp = [0] * len(s)
        for i, c in enumerate(s):
            if c == ')' and heap and heap[-1][1] == '(':
                l_i,_ = heap.pop()
                dp[l_i] = 1
                dp[i] = 1
            else:
                heap.append((i,c))

        for i in range(len(dp)):
            if dp[i]==1 and i>0:
                dp[i] = max(dp[i-1]+1,dp[i])
        if not dp:
            return 0
        return max(dp)

print(Solution().longestValidParentheses("()()"))

