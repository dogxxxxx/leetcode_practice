"""
Method 1:
Binary Search

Time complexity: O(nlog(n))
Space complexity: O(1)
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num
        while low <= high:
            mid = low + (high - low) // 2
            if mid == num / mid:
                return True
            elif mid > num / mid:
                high = mid - 1
            else:
                low = mid + 1
        return False


if __name__ == "__main__":
    num = 9 
    result = Solution().isPerfectSquare(num)
    print(result)