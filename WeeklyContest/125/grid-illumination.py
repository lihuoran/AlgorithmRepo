import collections

class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        row = collections.Counter()
        col = collections.Counter()
        ldiag = collections.Counter()
        rdiag = collections.Counter()
        on = set([])

        def turnOn(x, y):
            row[x] += 1
            col[y] += 1
            ldiag[x - y] += 1
            rdiag[x + y] += 1
            on.add((x, y))

        def turnOff(x, y):
            row[x] -= 1
            col[y] -= 1
            ldiag[x - y] -= 1
            rdiag[x + y] -= 1
            on.remove((x, y))

        def isOn(x, y):
            return any([row[x] > 0, col[y] > 0, ldiag[x - y] > 0, rdiag[x + y] > 0])

        for x, y in lamps:
            turnOn(x, y)
        ans = []
        for x, y in queries:
            ans.append(1 if isOn(x, y) else 0)
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if (i, j) in on:
                        turnOff(i, j)

        return ans
