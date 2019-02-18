class Solution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        a = A[::-1]
        n = len(a)
        k = K

        a[0] += k
        i = 0
        while True:
            if a[i] < 10:
                break
            else:
                if i == n - 1:
                    a.append(0)
                    n += 1
                a[i + 1] += a[i] // 10
                a[i] %= 10
                i += 1
        return a[::-1]