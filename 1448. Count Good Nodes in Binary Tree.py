from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
Method 1:
Keep the maximum value in the path
Use a global variable to store the result.

Time complexity: O(N)
Space complexity: O(h)
"""

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.result = 0
        def recursive(root, maximum):
            if not root:
                return
            if root.val >= maximum:
                self.result += 1
                recursive(root.left, root.val)
                recursive(root.right, root.val)
            else:
                recursive(root.left, maximum)
                recursive(root.right, maximum)
        recursive(root, float('-inf'))
        return self.result
    
"""
Method 2:
dfs

Time complexity: O(N)
Space complexity: O(h)
"""

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maximum):
            if not root:
                return 0
            if root.val >= maximum:
                return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
            else:
                return dfs(root.left, maximum) + dfs(root.right, maximum)
        return dfs(root, float("-inf"))
    