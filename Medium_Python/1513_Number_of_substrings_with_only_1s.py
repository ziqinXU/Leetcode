class Solution:
    def numSub(self, s: str) -> int:
        oneslist=[]
        i=0
        while i< len(s):
            if s[i]=='1':
                j=i
                while j<len(s) and s[j]=='1':
                    j=j+1
                oneslist.append(j-i)
                i=j
            else:
                i=i+1
        onessum=0
        for i in range(len(oneslist)):
            onessum=onessum+int((oneslist[i]+1)*(oneslist[i])//2)%(1000000007)
        
        return int(onessum)
