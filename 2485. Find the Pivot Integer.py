"""
Method 1:
Math

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(n, n//2, -1):
            if 2 * i * i - n * n - n == 0:
                return i
        return -1
    
"""
Method 2:
Keep left sum and right sum

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def pivotInteger(self, n: int) -> int:
        left_sum = sum(range(n + 1))
        right_sum = 0
        for i in range(n, n//2, -1):
            right_sum += i
            if right_sum == left_sum:
                return i
            left_sum -= i
        return -1
    

if __name__ == "__main__":
    n = 8
    result = Solution().pivotInteger(n)
    print(result)