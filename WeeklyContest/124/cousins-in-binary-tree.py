# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root, p, f):
        if root is None:
            return
        
        self.level[root.val] = p
        self.parent[root.val] = f
        self.dfs(root.left, p + 1, root.val)
        self.dfs(root.right, p + 1, root.val)
    
    def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
        self.level = {}
        self.parent = {}
        
        self.dfs(root, 0, -1)
        
        return self.level[x] == self.level[y] and self.parent[x] != self.parent[y]
