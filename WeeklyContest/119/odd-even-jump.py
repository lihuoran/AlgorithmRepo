class Solution:
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def findJump(A):
            import bisect
            vlist = [] # list of values
            v2idx = {} # value => closest index

            n = len(A)
            jump = [-1] * n
            for i in range(n)[::-1]:
                if i == n - 1 or A[i] > vlist[-1]:
                    pass # cannot jump from this point
                else:
                    idx = bisect.bisect_left(vlist, A[i])
                    # bisect.bisect_left guarantees that:
                    #   vlist[idx - 1] < A[i], vlist[idx] >= A[i]
                    # So vlist[idx] is the smallest element that is no smaller than A[i]
                    jump[i] = v2idx[vlist[idx]]

                if A[i] not in v2idx:
                    bisect.insort_right(vlist, A[i]) # Insert A[i] into vlist and keep vlist ordered
                v2idx[A[i]] = i # Update v2idx
            return jump

        ojump = findJump(A)
        ejump = findJump([-e for e in A])

        opossible = [False] * len(A)
        epossible = [False] * len(A)
        ans = 0
        for i in range(len(A))[::-1]:
            if i == len(A) - 1:
                opossible[i] = epossible[i] = True
            else:
                opossible[i] = epossible[ojump[i]] if ojump[i] != -1 else False
                epossible[i] = opossible[ejump[i]] if ejump[i] != -1 else False

            if opossible[i]:
                ans += 1
        return ans
