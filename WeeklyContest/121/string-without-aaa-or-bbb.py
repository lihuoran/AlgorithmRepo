class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        ret = ''
        for _ in range(A + B):
            if A > B:
                if len(ret) >= 2 and ret[-2:] == 'aa':
                    ret += 'b'
                    B -= 1
                else:
                    ret += 'a'
                    A -= 1
            else:
                if len(ret) >= 2 and ret[-2:] == 'bb':
                    ret += 'a'
                    A -= 1
                else:
                    ret += 'b'
                    B -= 1
        return ret
