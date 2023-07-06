"""
Method 1:
If the price at a day is lower than the price of a day after the day, buy the stock and sell it a day after the day.

Time complexity: O(N)
space complexity: O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]
        return profit
