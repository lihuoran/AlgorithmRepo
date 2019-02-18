import collections

class Solution:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        def count(a, k):
            need = k
            ans = 0
            i = 0
            cnt = collections.Counter()
            for j, e in enumerate(a):
                cnt[e] += 1
                if cnt[e] == 1:
                    need -= 1
                while need < 0:
                    cnt[a[i]] -= 1
                    if cnt[a[i]] == 0:
                        need += 1
                    i += 1
                ans += j - i + 1
            return ans
        
        return count(A, K) - count(A, K - 1)
                