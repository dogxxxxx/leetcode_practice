"""
Method 1:
Binary Search

Time complexity: O(log(n))
Space complexity: O(1)
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        while low <= high:
            mid = low + (high - low) // 2
            if mid == x / mid:
                return mid
            elif mid < x / mid:
                low = mid + 1
            else:
                high = mid - 1
        return high


if __name__ == "__main__":
    sol = Solution()
    x = 2
    result = sol.mySqrt(x)
    print(result)