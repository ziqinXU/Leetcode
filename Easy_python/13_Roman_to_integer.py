class Solution:
    def romanToInt(self, s: str) -> int:
        diction={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        totalsum=0
        for i in range(len(s)):
            totalsum=diction[s[i]]+totalsum
        for i in range(0,len(s)-1):
            if s[i]=='I' and (s[i+1]=='V' or s[i+1]=='X'):
                totalsum=totalsum-diction[s[i]]*2
            if s[i]=='X' and (s[i+1]=='L' or s[i+1]=='C'):
                totalsum=totalsum-diction[s[i]]*2
            if s[i]=='C' and (s[i+1]=='D' or s[i+1]=='M'):
                totalsum=totalsum-diction[s[i]]*2
            

        return totalsum
