from typing import List
"""
Method 1:
Store the accumulated 2s and 5s and change grid to
the number of 2s and 5s for each element.
Loop through the grid and calculate the 4 different
paths and get the max amount of trailing zeros.

Time complexity: O(m*n)
Space complexity: O(m*n)
"""

class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        def count_2s(n: int):
            count = 0
            while n and n % 2 == 0:
                n >>= 1
                count += 1
            return count
        
        def count_5s(n):
            count = 0
            while n and n % 5 == 0:
                n //= 5
                count += 1
            return count
        
        m, n = len(grid), len(grid[0])
        up = [[[0, 0] for _ in range(n)] for _ in range(m)]
        left = [[[0, 0] for _ in range(n)] for _ in range(m)]
        result = 0

        for i in range(m):
            for j in range(n):
                grid[i][j] = [count_2s(grid[i][j]), count_5s(grid[i][j])]
                up[i][j][0] = up[i-1][j][0] + grid[i][j][0]
                up[i][j][1] = up[i-1][j][1] + grid[i][j][1]
                left[i][j][0] = left[i][j-1][0] + grid[i][j][0]
                left[i][j][1] = left[i][j-1][1] + grid[i][j][1]
        
        for i in range(m):
            for j in range(n):
                upleft = [up[i][j][k] + left[i][j][k] - grid[i][j][k] for k in range(2)]
                upright = [up[i][j][k] + left[i][-1][k] - left[i][j][k] for k in range(2)]
                downleft = [up[-1][j][k] + left[i][j][k] - up[i][j][k] for k in range(2)]
                downright = [up[-1][j][k] - up[i][j][k] + left[i][-1][k] - left[i][j][k] + grid[i][j][k] for k in range(2)]
                trailing_zeros = max(min(upleft), min(upright), min(downleft), min(downright))
                result = max(result, trailing_zeros)
        return result
    

if __name__ == "__main__":
    grid = [[4,3,2],[7,6,1],[8,8,8]]
    result = Solution().maxTrailingZeros(grid)
    print(result)