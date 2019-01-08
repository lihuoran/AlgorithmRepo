class Solution:
    def isRationalEqual(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def decompose(s):
            if '.' not in s:
                return s, '', '0'

            integer = s.split('.')[0]
            if '(' in s:
                nonrepeat = s.split('.')[1].split('(')[0]
                repeat = s.split('.')[1].split('(')[1][:-1]
            else:
                nonrepeat = s.split('.')[1]
                repeat = '0'
            return integer, nonrepeat, repeat

        def shorten(s):
            if len(s) <= 1:
                return s
            if len(s) == 2 and s[0] == s[1]:
                return s[0]
            if len(s) == 3 and s[0] == s[1] == s[2]:
                return s[0]
            if len(s) == 4 and s[0] == s[1] == s[2] == s[3]:
                return s[0]
            if len(s) == 4 and s[:2] == s[2:]:
                return s[:2]
            return s

        def increment(integer, nonrepeat):
            if len(nonrepeat) == 0:
                return str(int(integer) + 1), nonrepeat
            else:
                nonrepeat = nonrepeat[:-1] + str(int(nonrepeat[-1]) + 1)
                return integer, nonrepeat

        def convert(integer, nonrepeat, repeat):
            repeat = shorten(repeat)

            while len(nonrepeat) >= len(repeat) and nonrepeat[-len(repeat):] == repeat:
                nonrepeat = nonrepeat[:-len(repeat)]

            if repeat == '9':
                repeat = '0'
                integer, nonrepeat = increment(integer, nonrepeat)
            else:
                for i in range(1, min(len(nonrepeat) + 1, len(repeat)))[::-1]:
                    if nonrepeat[-i:] == repeat[-i:]:
                        nonrepeat = nonrepeat[:-i]
                        repeat = repeat[-i:] + repeat[:-1]
                        break

            return integer, nonrepeat, repeat

        i1, n1, r1 = decompose(S)
        i2, n2, r2 = decompose(T)
        return convert(i1, n1, r1) == convert(i2, n2, r2)
