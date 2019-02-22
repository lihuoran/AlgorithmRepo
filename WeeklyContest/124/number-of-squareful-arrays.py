class Solution:
    def dfs(self, x):
        if x == self.n:
            self.ans += 1
            return

        last = None
        for i, val in enumerate(self.a):
            if self.usable[i]:
                if val == last:
                    continue
                if x != 0 and (val + self.rec[x - 1]) not in self.square:
                    continue

                self.usable[i] = False
                self.rec[x] = val
                self.dfs(x + 1)
                self.usable[i] = True
                last = val

    def numSquarefulPerms(self, A: 'List[int]') -> 'int':
        self.square = set([i ** 2 for i in range(32000)])
        self.ans = 0
        self.a = sorted(A)
        self.n = len(self.a)

        self.usable = [True] * self.n
        self.rec = [None] * self.n
        self.dfs(0)
        return self.ans

