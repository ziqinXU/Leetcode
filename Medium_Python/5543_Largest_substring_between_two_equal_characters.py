class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dislist=[]
        for i in range(len(s)):
            for j in reversed(range(i+1,len(s))):
                if s[i]==s[j]:
                    dislist.append(j-i-1)
        if len(dislist)!=0:
            return max(dislist)
        else:
            return -1
        
