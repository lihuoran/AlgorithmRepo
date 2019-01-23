class Solution:
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        c = len(grid[0])
        
        def idx(i, j):
            return i * c + j
    
        def contain(i, j, status):
            return status & (1 << idx(i, j)) != 0
        
        target = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    si, sj = i, j
                if grid[i][j] == 2:
                    ei, ej = i, j
                if grid[i][j] != -1:
                    target |= 1 << idx(i, j)
        
        dp = {}
        dp[(idx(si, sj), 1 << idx(si, sj))] = 1
        
        def calc(i, j, status):
            if not contain(i, j, status):
                return 0
            
            if (idx(i, j), status) not in dp:
                cur = 0
                for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if not (0 <= x < r and 0 <= y < c and grid[x][y] != -1):
                        continue
                    cur += calc(x, y, status - (1 << idx(i, j)))
                dp[(idx(i, j), status)] = cur
            return dp[(idx(i, j), status)]
        return calc(ei, ej, target)
