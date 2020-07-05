class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops)>0:
            zipped = list(zip(*ops))
            return min(zipped[0])*min(zipped[1])
        else:
            return m*n
