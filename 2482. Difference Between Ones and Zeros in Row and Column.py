"""
Method 1:
Calculate row difference and column difference first and modify the original grid.

Time complexity: O(N * M)
Space complexity: O(N + M) for N, M = len(rows), len(columns)
"""

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        columns = len(grid[0])
        row_diff = []
        column_diff = []
        for i in range(rows):
            row_diff.append(2 * sum(grid[i]) - columns)

        column_diff = [2 * sum(column) - rows for column in zip(*grid)]
        
        for i in range(rows):
            for j in range(columns):
                grid[i][j] = row_diff[i] + column_diff[j]
        return grid
