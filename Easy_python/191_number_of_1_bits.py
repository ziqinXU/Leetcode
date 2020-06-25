class Solution:
    def hammingWeight(self, n: int) -> int:
        A=str(bin(n))
        return A.count('1')
