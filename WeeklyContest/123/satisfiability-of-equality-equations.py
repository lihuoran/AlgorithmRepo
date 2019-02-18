class Solution:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        parent = {c: c for c in 'abcdefghijklmnopqrstuvwxyz'}

        def root(x):
            if parent[x] != x:
                parent[x] = root(parent[x])
            return parent[x]

        def merge(x, y):
            parent[root(x)] = root(y)

        equations.sort(key=lambda x: 0 if x[1] == '=' else 1)
        for eq in equations:
            a, b, relation = eq[0], eq[-1], eq[1:-1]
            if relation == '==':
                merge(a, b)
            else:
                if root(a) == root(b):
                    return False
        return True
