class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        import math
        candidate_x = [1] if x == 1 else [x ** i for i in range(0, math.ceil(math.log(bound, x)) + 1)]
        candidate_y = [1] if y == 1 else [y ** i for i in range(0, math.ceil(math.log(bound, y)) + 1)]
        result_set = set(ex + ey for ex in candidate_x for ey in candidate_y if ex + ey <= bound)
        return list(result_set)
    