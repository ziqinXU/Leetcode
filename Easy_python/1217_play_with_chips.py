class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        odd=0
        even=0
        #计算奇数和偶数位置上的砝码数量，移动较少的一种，每个仅需1步至奇数或偶数位置
        for i in range(len(chips)):
            if chips[i]%2==0:
                even=even+1
            if chips[i]%2==1:
                odd=odd+1
        if even>odd:
            return odd
        else:
            return even

