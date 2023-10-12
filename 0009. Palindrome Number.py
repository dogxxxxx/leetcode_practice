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
        mid = len(x) // 2
        if len(x) % 2 == 0:
            for i in range(mid):
                if x[mid - i - 1] != x[mid + i]:
                    return False
        else:
            for i in range(1, mid + 1):
                if x[mid - i] != x[mid + i]:
                    return False
        return True

"""
Method 2:
Get the reversed number of the last half part of x.

Time complexity: O(N/2)
Space complexity: O(1)
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False

        reverse = 0
        while reverse < x:
            reverse = reverse * 10 + x % 10
            x = x // 10

        if reverse == x or reverse // 10 == x:
            return True
        else:
            return False
