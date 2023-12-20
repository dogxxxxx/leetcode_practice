from typing import List
"""
Method 1:
Sort prices first then get 2 cheapest chocolate.

Time complexity: O(nlog(n))
Space complexity: O(1)
"""

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices = sorted(prices)
        result = money - prices[0] - prices[1]
        return result if result >= 0 else money

"""
Method 2:
Loop through the price list and find 2 cheapest chocolates.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        p1, p2 = 100, 100
        for p in prices:
            if p < p1:
                p1, p2 = p, p1
            elif p < p2:
                p2 = p
        result = money - p1 - p2
        return result if result >= 0 else money

if __name__ == "__main__":
    sol = Solution()
    prices = [1,2,2]
    money = 3
    result = sol.buyChoco(prices, money)
    print(result)