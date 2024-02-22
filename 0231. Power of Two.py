"""
Method 1:
Count the bits

Time complexity:
Space complexity: O(1)
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0 or n.bit_count() != 1:
            return False
        else:
            return True

"""
Method 2:
bitwise operation

Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0 or n & (n - 1) != 0:
            return False
        else:
            return True


if __name__ == "__main__":
    n = 64
    result = Solution().isPowerOfTwo(n)
    print(result)
