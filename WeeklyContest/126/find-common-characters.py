class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        candidate = 'abcdefghijklmnopqrstuvwxyz'
        cnt = collections.Counter()
        for c in candidate:
            cnt[c] = float('inf')

        for e in A:
            cur = collections.Counter(e)
            for c in candidate:
                cnt[c] = min(cnt[c], cur[c])

        ret = []
        for k, v in cnt.items():
            if v > 0:
                ret += [k] * v
        return ret
