class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #dp第一位为True，遍历j，当之前的dp[i]为TRue且之间的string在word中时，当前j也标记为True
        dp=[False]*(len(s)+1)
        dp[0]=True
        j=0
        while j<len(s):
            for i in range(j+1):
                if dp[i]==True and s[i:j+1] in wordDict:
                    dp[j+1]=True
                    break
            j=j+1
        return dp[-1]
