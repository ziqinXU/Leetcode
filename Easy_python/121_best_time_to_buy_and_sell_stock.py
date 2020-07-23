class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxval=0
        for i in range(len(prices)):
            if max(prices[i:])>prices[i]:
                diff=max(prices[i:])-prices[i]
                if diff>maxval:
                    maxval=diff
        return maxval
