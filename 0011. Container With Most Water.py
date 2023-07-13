"""
Method 1:
Get the area between the first and the last index.
Then make the shorter side one index closer to the longer side and calculate area.

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        def get_area(h1, h2, length):
            area = min(h1, h2) * length
            return area
        
        h1 = 0
        h2 = len(height) - 1
        result = 0
        while h1 < h2:
            area = get_area(height[h1], height[h2], h2-h1)
            result = max(area, result)
            if height[h1] <= height[h2]:
                h1 += 1
            else:
                h2 -= 1
        return result
