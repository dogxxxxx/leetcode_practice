from typing import List
"""
Method 1:
Sort the coin array first and count the number of additions.
If x + 1 is added, then the next number to be considered to add
is 2 * x + 1. This is the most important concept in this question.

Time complexity: O(N * log(N))
Space complexity: O(1)
"""

class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        current_max = 0
        index = 0
        res = 0

        while current_max < target:
            if index < len(coins) and current_max + 1 >= coins[index]:
                current_max += coins[index]
                index += 1
            else:
                current_max += current_max + 1
                res += 1

        return res
