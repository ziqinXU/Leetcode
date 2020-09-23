class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if(len(pairs)==0):
            return 0
        pairs.sort(key=lambda k:k[0])
        dp=[0]*len(pairs)
        for i in range(len(pairs)):
            dp[i]=1
            for j in reversed(range(0,i)):
                if pairs[i][0]>pairs[j][1]:
                    dp[i]=max(dp[j]+1,dp[i])
                    break
        return max(dp)
