class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        dp=[0]*len(A)
        if len(A)<=2:
            return 0
        dp[0]=0
        dp[1]=0
        if A[2]-A[1]==A[1]-A[0]:
            dp[2]=1
        for i in range(3,len(A)):
            if A[i]-A[i-1]==A[i-1]-A[i-2]: ####
                dp[i]=dp[i-1]+1
            else:
                dp[i]=0
        return sum(dp)
