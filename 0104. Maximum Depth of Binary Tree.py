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

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, result):
            if not root:
                return result
            return max(dfs(root.left, result + 1), dfs(root.right, result + 1))
        result = dfs(root, 0)
        return result