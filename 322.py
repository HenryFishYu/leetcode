from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [10001] * (amount+1)
        dp[-1] = 0
        for i in range(amount-1,-1,-1):
            for coin in coins:
                if i+coin<=amount:
                    dp[i] = min(dp[i],dp[i+coin]+1)

        return dp[0] if dp[0]!=10001 else -1

print(Solution().coinChange([1,2,5],11))

