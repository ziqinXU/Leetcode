class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        A=s.split()
        if len(A)==0:
            return 0
        return len(A[-1])
