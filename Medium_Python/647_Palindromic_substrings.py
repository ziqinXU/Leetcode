class Solution:
    def countSubstrings(self, s: str) -> int:
        dp=[[False]*len(s) for i in range(len(s))]
        count=0
        for j in range(0,len(s)):
            for i in range(0,j+1):
                if s[i]==s[j] and (j-i<2 or dp[i+1][j-1]==True):
                    dp[i][j]=True
                    count=count+1
                
        return count
