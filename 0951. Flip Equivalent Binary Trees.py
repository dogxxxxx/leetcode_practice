from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
Method 1:
DFS

Need to practice later!
"""

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(r1, r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2 or r1.val != r2.val:
                return False
            return ((dfs(r1.left, r2.left) or dfs(r1.left, r2.right)) and (dfs(r1.right, r2.right) or dfs(r1.right, r2.left)))
        return dfs(root1, root2)
    
