class Solution:
    def countTriplets(self, A: 'List[int]') -> 'int':
        tot = 1 << 16
        cnt = [0 for _ in range(tot)]
        for a in A:
            for b in A:
                cnt[a & b] += 1
        
        ans = 0
        for e in A:
            s = 0
            while s < tot:
                if s & e == 0:
                    ans += cnt[s]
                    s += 1
                else:
                    s += (e & s)
        return ans
