class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        s = 0
        for e in A:
            if e % 2 == 0:
                s += e
        
        ans = []
        for val, idx in queries:
            if A[idx] % 2 == 0:
                s -= A[idx]
            A[idx] += val
            if A[idx] % 2 == 0:
                s += A[idx]
            ans.append(s)
        return ans
