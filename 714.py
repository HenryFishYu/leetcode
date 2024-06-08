from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        res = 0
        buy = prices[0]
        for price in prices[1:]:
            if price<buy:
                buy = price
                continue

            if price-fee>buy:
                res += price-buy
                buy = price-2
        return res

