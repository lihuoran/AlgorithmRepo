class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    si, sj = i, j

        ans = 0
        for mx, my in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = si, sj
            x += mx
            y += my
            while (0 <= x < 8 and 0 <= y < 8 and board[x][y] == '.'):
                x += mx
                y += my
            if 0 <= x < 8 and 0 <= y < 8 and board[x][y] == 'p':
                ans += 1
        return ans
