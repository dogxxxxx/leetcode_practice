from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
Method 1:
This is easy because it is BST.

Time complexity: O(log(N))
Space complexity: O(1)
"""

class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        small = min(p.val, q.val)
        large = max(p.val, q.val)
        while True:
            current = root.val
            if small <= current <= large:
                return current
            elif root.val < small:
                root = root.left
            else:
                root = root.right

