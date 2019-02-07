class Solution:
    def i2c(self, i):
        return 'abcdefghijklmnopqrstuvwxyz'[i]
    
    def dfs(self, root, cur):
        s = cur + self.i2c(root.val)
        
        if root.left is None and root.right is None:
            self.pool.append(s)
            return
        if root.left is not None:
            self.dfs(root.left, s)
        if root.right is not None:
            self.dfs(root.right, s)
    
    def smallestFromLeaf(self, root: 'TreeNode') -> 'str':
        self.pool = []
        self.dfs(root, '')
        self.pool = [e[::-1] for e in self.pool]
        return min(self.pool)
