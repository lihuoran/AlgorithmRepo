class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        cntzero = 0
        i = -1
        ans = 0
        for j, val in enumerate(A):
            cntzero += 1 if val == 0 else 0
            while cntzero > K:
                i += 1
                cntzero -= 1 if A[i] == 0 else 0
            ans = max(ans, j - i)
        return ans
