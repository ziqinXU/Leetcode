class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        for idx,number in enumerate(A):
            if idx==number:
                return idx
        return -1
