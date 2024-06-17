"""
Method 1:
Binary search in range of max possibility

Time complexity: O(Nlog(N)), N is the square root of c
Space complexity: O(1)
"""

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        top = int(c ** (1 / 2))
        while top >= 0:
            up = top
            down = 0
            mid = (up + down) // 2
            while up >= down:
                res = mid ** 2 + top ** 2
                if res == c:
                    return True
                elif res > c:
                    up = mid - 1
                    mid = (down + up) // 2
                else:
                    down = mid + 1
                    mid = (up + down) // 2
            top -= 1
        return False

"""
Method 2:
Two pointers

Time complexity: O(N), N is the sqrt of c
Space complexity: O(1)
"""

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c ** (1 / 2))
        while left <= right:
            res = left ** 2 + right ** 2
            if res < c:
                left += 1
            elif res > c:
                right -= 1
            else:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    c = 5
    res = sol.judgeSquareSum(c)
    print(res)
