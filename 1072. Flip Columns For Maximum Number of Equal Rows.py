from typing import List
from collections import defaultdict, Counter
"""
Method 1:
Flip the rows that start with 0. Then the row pattern that shows most frequently is the answer.

Time complexity: O(m * n)
Space complexity: O(m)
"""

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern = defaultdict(int)
        for row in matrix:
            if row[0] == 0:
                pattern[str(row)] += 1
            else:
                row = [i ^ 1 for i in row]
                pattern[str(row)] += 1
        
        return max(pattern.values())


if __name__ == "__main__":
    matrix = [[0,1],[1,1]]
    res = Solution().maxEqualRowsAfterFlips(matrix)
    print(res)
