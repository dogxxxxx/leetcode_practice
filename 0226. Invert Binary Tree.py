from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
Method 1:
Recursive

Time complexity: O(N)
Space complexity: O(h)
"""

class Solution:
    def change(self, root):
        root.left, root.right = root.right, root.left
        return root
    

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recursive(root):
            if root == None:
                return root
            root.left, root.right = root.right, root.left
            if root.left:
                recursive(root.left)
            if root.right:
                recursive(root.right)
            return root
        res = recursive(root)
        return res