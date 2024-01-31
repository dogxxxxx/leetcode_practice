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
    def compare(self, p, q):
        if not p and not q:
            return
        elif not p or not q:
            self.result = False
            return
        if p.val != q.val:
            self.result = False
            return
        self.compare(p.left, q.left)
        self.compare(p.right, q.right)


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.result = True
        self.compare(p, q)
        return self.result
    