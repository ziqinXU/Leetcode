class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        returnarray=[None]*len(A)
        odd=1#奇数
        even=0#偶数
        for i in range(len(A)):
            if A[i]%2==0:
                returnarray[even]=A[i]
                even=even+2
            else:
                returnarray[odd]=A[i]
                odd=odd+2
        return returnarray
