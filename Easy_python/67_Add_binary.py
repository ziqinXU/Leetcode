class Solution:
    def addBinary(self, a: str, b: str) -> str:
        A=bin(int(a,2)+int(b,2))
        return A[2:]
