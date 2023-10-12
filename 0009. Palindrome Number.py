"""
Method 1:
Get the index of the middle in x and compare
the letter one by one until reaching the head of x.

Time complexity: O(N/2)
Space complexity: O(1)
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if len(x) % 2 == 0:
            mid = int(len(x) / 2)
            for i in range(mid):
                if x[mid - i - 1] != x[mid + i]:
                    return False
        else:
            mid = int(len(x) / 2)
            for i in range(1, mid + 1):
                if x[mid - i] != x[mid + i]:
                    return False
        return True
