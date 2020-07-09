class Solution:
    def sortString(self, s: str) -> str:
        resultstring=""
        totallen=len(s)
        count=0
        A=Counter(s)
        while count<totallen:
            for i in sorted(A):#sorted(A)=['a','b','c']
                if A[i]!=0:
                    count=count+1
                    A[i]=A[i]-1
                    resultstring=resultstring+i
            
            for i in reversed(sorted(A)):
                if A[i]!=0:
                    count=count+1
                    A[i]=A[i]-1
                    resultstring=resultstring+i
        return resultstring
