class Sum:
    def __init__(self, A):
        self.prefix = [0]
        for val in A:
            self.prefix.append(self.prefix[-1] + val)

    def getsum(self, i, j):
        return self.prefix[j + 1] - self.prefix[i]

class Solution:
    def mergeStones(self, stones, K):
        n = len(stones)
        s = Sum(stones)
        f = [[[-1 for _ in range(n + 1)] for _ in range(n)] for _ in range(n)]
        for width in range(1, n + 1):
            for i in range(n - width + 1):
                j = i + width - 1
                for m in range(1, width + 1)[::-1]:
                    if (width - m) % (K - 1) != 0:
                        continue

                    if m == width:
                        f[i][j][m] = 0
                    elif m == 1:
                        f[i][j][m] = f[i][j][K] + s.getsum(i, j)
                    else:
                        f[i][j][m] = min(f[i][t][1] + f[t + 1][j][m - 1] for t in range(i, j, K - 1))
        return f[0][n - 1][1]
