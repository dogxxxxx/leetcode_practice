from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
Method 1:
Keep all values in a level and
append the last value to result.

Time complexity: O(N)
Space complexity: O(h)
"""

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        result = []
        current_level = []
        queue.append("next")
        while queue:
            current = queue.popleft()
            if current == "next":
                if len(current_level) != 0:
                    result.append(current_level[-1])
                    current_level = []
                    queue.append("next")
                continue
            current_level.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result
            
"""
Method 2:
Traverse the right side first.
Then, the first element in a level
is the rightest.

Time complexity: O(N)
Space complexity: O(h)
"""

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        seen = set()
        def get_right(root, level):
            if not root:
                return
            if level not in seen:
                result.append(root.val)
                seen.add(level)
            get_right(root.right, level + 1)
            get_right(root.left, level + 1)
        get_right(root, 0)
        return result

