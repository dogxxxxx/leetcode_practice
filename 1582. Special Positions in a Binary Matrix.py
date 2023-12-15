"""
Method 1:
Store the index of row and column that the sum is 1.

Time complexity: O(n * m)
Space complexity: O(n + m)
"""

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        row_ind = [index for index, row in enumerate(mat) if sum(row) == 1]
        column_ind = [index for index, col in enumerate(zip(*mat)) if sum(col) == 1]

        for r in row_ind:
            for c in column_ind:
                if mat[r][c] == 1:
                    count += 1
        
        return count
