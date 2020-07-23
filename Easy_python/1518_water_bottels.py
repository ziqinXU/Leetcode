class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        numberempty=numBottles
        totalsum=numBottles
        while int(numberempty/numExchange)!=0:
            totalsum=totalsum+int(numberempty/numExchange)
            numberempty=int(numberempty/numExchange)+numberempty%numExchange
        return totalsum
