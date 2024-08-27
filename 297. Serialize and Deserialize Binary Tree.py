# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serialized_lst = []
        def dfs(root):
            if not root:
                serialized_lst.append("N")
                return
            
            serialized_lst.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(serialized_lst)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        serialize_lst = data.split(",")
        self.index = 0
        def dfs():
            if serialize_lst[self.index] == "N":
                self.index += 1
                return None
            
            root = TreeNode(int(serialize_lst[self.index]))
            self.index += 1
            
            root.left = dfs()
            root.right = dfs()

            return root
        return dfs()