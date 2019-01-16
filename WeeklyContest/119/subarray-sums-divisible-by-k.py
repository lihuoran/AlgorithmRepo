class Solution:
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        s = [0]
        for e in A:
            s.append(s[-1] + e)
        s = [e % K for e in s]
        
        import collections
        cnt = collections.Counter(s)
        return sum(v * (v - 1) // 2 for v in cnt.values())
