class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        A=Counter(s)
        B=Counter(t)
        for i in B:
            if B[i]>A[i]:
                return i
