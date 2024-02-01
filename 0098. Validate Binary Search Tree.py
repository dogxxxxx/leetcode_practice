from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
Method 1:
dfs
"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, small, large):
            if not root:
                return True
            if not small < root.val < large:
                return False
            return dfs(root.left, small, root.val) and dfs(root.right, root.val, large)
        return dfs(root, float('-inf'), float('inf'))
    