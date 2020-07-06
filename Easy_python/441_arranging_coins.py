class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1+sqrt(n*8+1))/2)
