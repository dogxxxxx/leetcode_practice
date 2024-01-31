from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
"""
Method 1:
Use queue.
Key: append sign to change level.

Time complexity: O(N)
Space complexity: O(N)
"""

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        result = []
        current_level = []
        queue.append("next")
        while queue:
            cur = queue.popleft()
            if cur == "next":
                if len(current_level) != 0:
                    result.append(current_level)
                    current_level = []
                    queue.append("next")
                continue
            current_level.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return result
