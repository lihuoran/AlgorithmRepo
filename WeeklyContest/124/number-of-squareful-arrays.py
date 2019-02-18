class Solution:
    def dfs(self, x):
        if x == self.n:
            self.ans += 1
            return

        for i in range(self.n):
            if self.mark[i]:
                continue
            cur = self.a[i]
            if i != 0 and self.mark[i - 1] == False and self.a[i] == self.a[i - 1]:
                continue
            if x != 0 and (cur + self.rec[x - 1]) not in self.square:
                continue

            self.mark[i] = True
            self.rec[x] = cur
            self.dfs(x + 1)
            self.mark[i] = False

    def numSquarefulPerms(self, A: 'List[int]') -> 'int':
        self.square = set([i ** 2 for i in range(32000)])
        self.ans = 0
        self.a = sorted(A)
        self.n = len(self.a)

        self.mark = [False for _ in range(self.n)]
        self.rec = [None for _ in range(self.n)]
        self.dfs(0)
        return self.ans
