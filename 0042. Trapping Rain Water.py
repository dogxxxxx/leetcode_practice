"""
Method 1:
Calculate occupied area from row 0 to the tallest row.
Subtract the sum of height, which is the area occupied at first.

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        p1 = 0
        p2 = len(height) - 1
        height_diff = 0
        height_now = 0
        while p1 != p2:
            height_diff = min(height[p1], height[p2]) - height_now
            height_now = min(height[p1], height[p2])
            result += height_diff * (p2-p1+1)
            if height[p1] == height[p2]:
                cp1 = p1
                cp2 = p2
                while height[p1] <= height[cp1] and p1 < p2:
                    p1 += 1
                while height[p2] <= height[cp2] and p1 < p2:
                    p2 -= 1
            elif height[p1] < height[p2]:
                cp1 = p1
                while height[p1] <= height[cp1] and p1 < p2:
                    p1 += 1
            else:
                cp2 = p2
                while height[p2] <= height[cp2] and p1 < p2:
                    p2 -= 1
        result += height[p2] - height_now
        return result - sum(height)
