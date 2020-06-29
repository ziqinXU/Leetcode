class Solution:
    import string
    def reformat(self, s: str) -> str:
        returnstring=[None]*len(s)
        A=string.ascii_lowercase
        alpha=0
        number=0
        alphalist=[]
        numberlist=[]
        for i in range(len(s)):
            if s[i] in A:
                alpha=alpha+1
                alphalist.append(s[i])
            else:
                numberlist.append(s[i])
        number=len(s)-alpha
        if abs(number-alpha)>1:
            return ""
        else:
            if number>=alpha:
                k=0
                for i in range(0,len(s),2):
                    returnstring[i]=numberlist[k]
                    k=k+1
                p=0
                for j in range(1,len(s),2):
                    returnstring[j]=alphalist[p]
                    p=p+1
            if number<alpha:
                k=0
                for i in range(0,len(s),2):
                    returnstring[i]=alphalist[k]
                    k=k+1
                p=0
                for j in range(1,len(s),2):
                    returnstring[j]=numberlist[p]
                    p=p+1
    
        return ''.join(returnstring)

        
