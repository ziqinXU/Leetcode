class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k=0
        k1=0
        for i in range(len(s)):
            k1=t.find(s[i],k)
            if k1==-1:
                return False
            k=k1+1
        return True
            
