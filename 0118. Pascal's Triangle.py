from typing import List
"""
Method 1:
Append a row to result in numrows

Time complexity: O(N**2)
Space complexity: O(N**2)
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        dp = [[] for _ in range(numRows)]
        dp[0] = [1]
        dp[1] = [1, 1]
        for i in range(2, numRows):
            dp[i].append(dp[i - 1][0])
            for j in range(len(dp[i - 1]) - 1):
                dp[i].append(dp[i - 1][j] + dp[i - 1][j + 1])
            dp[i].append(dp[i - 1][-1])
        return dp
    

if __name__ == "__main__":
    numRows = 5
    result = Solution().generate(numRows)
    print(result)