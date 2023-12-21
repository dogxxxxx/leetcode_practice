from typing import List
"""
Method 1:
Sort the points by second elementsand if the second elements are the same, sort by the first elements.
Then, loop over the sorted points and the arrow is at the same place as the second element.
Last, burst the balloon by popping them from the points.

Time complexity: O(nlogn))
Space complexity: O(1)
"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: (x[1], x[0]))
        result = 0
        while points:
            arrow = points[0][1]
            result += 1
            while points[0][0] <= arrow:
                points.pop(0)
                if not points:
                    break
        return result


if __name__ == "__main__":
    points = [[1,2],[2,3],[3,4],[4,5]]
    result = Solution().findMinArrowShots(points)
    print(result)