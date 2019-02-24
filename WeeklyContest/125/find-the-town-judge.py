class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        odeg = [0] * (N + 1)
        ideg = [0] * (N + 1)
        for a, b in trust:
            odeg[a] += 1
            ideg[b] += 1
        
        for i in range(1, N + 1):
            if odeg[i] == 0 and ideg[i] == N - 1:
                return i
        return -1
