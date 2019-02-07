class Solution:
    def dfs(self, root, x, y):
        if root is None:
            return
        
        if x not in self.pool:
            self.pool[x] = []
        self.pool[x].append((y, self.cnt, root.val))
        self.cnt += 1
        
        self.dfs(root.left, x - 1, y - 1)
        self.dfs(root.right, x + 1, y - 1)
    
    def verticalTraversal(self, root: 'TreeNode') -> 'List[List[int]]':
        self.pool = {}
        self.cnt = 0
        self.dfs(root, 0, 0)
        
        klist = sorted(list(self.pool.keys()))
        ans = []
        for k in klist:
            cur = self.pool[k]
            cur.sort(key=lambda x: (-x[0], x[2]))
            cur = [e[-1] for e in cur]
            ans.append(cur)
        return ans
