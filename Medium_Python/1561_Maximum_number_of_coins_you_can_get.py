#贪心算法
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
    #策略：让bob每次取走当前堆内最少的
        piles=sorted(piles,reverse=True)
        groups=len(piles)//3
        return sum(piles[1:len(piles)-groups:2])
