class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A = [number**2 for number in A]
        A.sort()
        return A
