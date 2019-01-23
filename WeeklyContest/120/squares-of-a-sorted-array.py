class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        a = [e ** 2 for e in A if e < 0][::-1]
        b = [e ** 2 for e in A if e >= 0]

        ret = []
        i = 0
        j = 0
        n = len(a)
        m = len(b)
        while i < n or j < m:
            if i == n:
                ret.append(b[j])
                j += 1
            elif j == m:
                ret.append(a[i])
                i += 1
            else:
                if a[i] < b[j]:
                    ret.append(a[i])
                    i += 1
                else:
                    ret.append(b[j])
                    j += 1
        return ret
