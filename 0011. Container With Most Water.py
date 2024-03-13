from typing import List
"""
Method 1:
Get the area between the first and the last index.
Then make the shorter side one index closer to the longer side and calculate area.

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1, p2 = 0, len(height) - 1
        result = 0
        while p2 > p1:
            area = min(height[p1], height[p2]) * (p2 - p1)
            result = max(result, area)
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1
        return result

"""
Method 2:
Same as Method 1. Just skip area calculation for some situations.

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
                while height[h1] <= height[h1-1] and h1 < h2:
                    h1 += 1
            else:
                h2 -= 1
                while height[h2] <= height[h2+1] and h1 < h2:
                    h2 -= 1
        return result
        

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    result = Solution().maxArea(height)
    print(result)
