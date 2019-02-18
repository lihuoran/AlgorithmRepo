import collections

class Solution:
    def minKBitFlips(self, A: 'List[int]', K: 'int') -> 'int':
        n = len(A)
        ans = 0
        flip = collections.deque()
        for i, val in enumerate(A):
            while len(flip) > 0 and i - flip[0] >= K:
                flip.popleft()
                
            if len(flip) % 2 == val:
                if i <= n - K:
                    ans += 1
                    flip.append(i)
                else:
                    return -1
        return ans
