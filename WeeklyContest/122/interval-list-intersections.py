class Solution:
    def intervalIntersection(self, A: 'List[Interval]', B: 'List[Interval]') -> 'List[Interval]':
        a = A
        b = B
        if len(a) == 0 or len(b) == 0:
            return []
        
        pool = [] # possible points
        for e in a:
            pool.append((e.start, 0)) # start of an interval of A
            pool.append((e.end, 2)) # end of an interval of A
        for e in b:
            pool.append((e.start, 1)) # start of an interval of B
            pool.append((e.end, 3)) # end of an interval of B
        pool.sort()

        marka = False # whether we are in an interval of A
        markb = False # whether we are in an interval of B
        ans = []
        l, r = None, None
        for pos, cate in pool:
            if cate == 0: # enter A
                marka = True
                if markb == True:
                    l = pos
            if cate == 1: # quit A
                markb = True
                if marka == True:
                    l = pos
            if cate == 2: # enter B
                if marka and markb:
                    r = pos
                    ans.append(Interval(l, r))
                marka = False
            if cate == 3: # quit B
                if marka and markb:
                    r = pos
                    ans.append(Interval(l, r))
                markb = False

        return ans
