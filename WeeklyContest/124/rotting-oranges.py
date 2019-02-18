class Solution:
    def orangesRotting(self, grid: 'List[List[int]]') -> 'int':
        n = len(grid)
        m = len(grid[0])
        
        import collections
        queue = collections.deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        
        ans = 0
        while len(queue) > 0: # BFS
            x, y, cnt = queue.popleft()
            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if not (0 <= i < n and 0 <= j < m and grid[i][j] == 1):
                    continue
                grid[i][j] = 2
                queue.append((i, j, cnt + 1))
                ans = max(ans, cnt + 1)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return ans
