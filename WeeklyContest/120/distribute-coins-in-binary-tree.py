class Solution:
    def work(self, root):
        if root is None:
            return 0

        l = self.work(root.left)
        r = self.work(root.right)
        cur = l + r + root.val
        self.ans += abs(cur - 1)

        return cur - 1

    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.work(root)
        return self.ans
