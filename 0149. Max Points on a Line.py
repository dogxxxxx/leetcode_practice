"""
Method 1:
Compute slope and intersect for every 2 points in the list.

Time complexity: O(N^2)
Space complexity: O(N)
"""

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        def get_slope_intersect(p1, p2):
            if p1[0] == p2[0]:
                return (p1[0], 'vertical')
            s = (p2[1]-p1[1]) / (p2[0]-p1[0])
            i = p2[1] - (s*p2[0])
            return (s, round(i, 5))

        result = 1
        for i in range(len(points) - 1):
            line = {}
            for j in range(i+1, len(points)):
                slope, intersect = get_slope_intersect(points[i], points[j])
                line[(slope, intersect)] = line.get((slope, intersect), 0) + 1
            result = max(result, max(line.values())+1)
        return result
