class Solution:
    def isValid(self, S: str) -> bool:
        while S.find('abc') != -1:
            S = S.replace('abc', '')
        return len(S) == 0
