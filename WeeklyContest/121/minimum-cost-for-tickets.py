class Solution:
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
        cover = [1, 7, 30]
        
        n = len(days)
        dp = [float('inf') for _ in range(n)]
        
        for i in range(n):
            prev = 0 if i == 0 else dp[i - 1] 
            for c, cost in zip(cover, costs):
                for j in range(i, n):
                    if days[j] - days[i] < c:
                        dp[j] = min(dp[j], prev + cost)
                    else:
                        break
        return dp[-1]
