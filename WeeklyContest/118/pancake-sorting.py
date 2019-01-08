class Solution:
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        def argmax(a, k):
            idx = 0
            for i in range(1, k + 1):
                if a[idx] < a[i]:
                    idx = i
            return idx
    
        def reverse(a, k):
            a[:k + 1] = a[:k + 1][::-1]
        
        n = len(A)
        ans = []
        for i in range(1, n)[::-1]:
            idx = argmax(A, i)
            if idx == i:
                continue
                
            if idx != 0:
                ans.append(idx + 1)
                reverse(A, idx)
            ans.append(i + 1)
            reverse(A, i)
        
        return ans
