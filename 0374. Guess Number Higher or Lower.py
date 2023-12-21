# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass
"""
Method 1:
Binary Search

Time complexity: O(log(n))
Space complexity: O(1)
"""

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = low + (high - low) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == 1:
                low = mid + 1
            else:
                high = mid - 1
