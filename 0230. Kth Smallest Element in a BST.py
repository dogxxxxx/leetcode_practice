from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
Method 1:
dfs, if the count equals k,
keep the val

Time complexity
"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = 0
        def dfs(root):
            if not root:
                return
            if root.left:
                dfs(root.left)
            self.count += 1
            if self.count == k:
                self.result = root.val
                return
            dfs(root.right)
        dfs(root)
        return self.result
    