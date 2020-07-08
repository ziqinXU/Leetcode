class Solution:
    def balancedStringSplit(self, s: str) -> int:
        #遍历，当当前分割子串中R与L数量相同时，计数+1
        i=0
        totalcount=0
        numberR=0
        numberL=0
        while i< len(s):
            if s[i]=='R':
                numberR=numberR+1
            else:
                numberL=numberL+1
            if numberR==numberL:
                totalcount=totalcount+1
            i=i+1
        return totalcount
            
