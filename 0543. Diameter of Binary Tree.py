from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
Method 1:

"""

class Solution:
    def calculate_depth(self, root):
        if not root:
            return 0
        left = self.calculate_depth(root.left)
        right = self.calculate_depth(root.right)
        self.result = max(left + right, self.result)
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.calculate_depth(root)
        return self.result