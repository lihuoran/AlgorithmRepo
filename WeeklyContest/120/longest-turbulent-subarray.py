class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        a = A
        n = len(a)

        p = [1 for _ in range(n)] # a[i] > a[i - 1]
        q = [1 for _ in range(n)] # a[i] < a[i - 1]
        for i in range(1, n):
            if a[i] == a[i - 1]:
                p[i] = q[i] = 1
            elif a[i] > a[i - 1]:
                p[i] = q[i - 1] + 1
                q[i] = 1
            else:
                p[i] = 1
                q[i] = p[i - 1] + 1

        return max(max(p), max(q))
