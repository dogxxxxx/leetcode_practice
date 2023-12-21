from typing import List
"""
Method 1:
Sort the points by the first element.
Then, iterate the points and find the max width.

Time complexity: O(Nlog(N))
Space complexity: O(1)
"""

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        result = float('-inf')
        points = sorted(points, key=lambda x: x[0])
        for i in range(len(points) - 1):
            result = max(points[i + 1][0] - points[i][0], result)
        return result
    

if __name__ == "__main__":
    points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
    result = Solution().maxWidthOfVerticalArea(points)
    print(result)
