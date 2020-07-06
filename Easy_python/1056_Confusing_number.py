class Solution:
    def confusingNumber(self, N: int) -> bool:
        good=['0','1','8']
        bad=['2','3','4','5','7']
        newnumber=list(str(N))
        newlist=[None]*len(newnumber)
        for i in range(len(newnumber)):
            if newnumber[i] in bad:
                return False
            elif newnumber[i] in good:
                newlist[len(newnumber)-1-i]=newnumber[i]
            else:               
                if newnumber[i]=='6':
                    newlist[len(newnumber)-1-i]='9'
                if newnumber[i]=='9':
                    
                    newlist[len(newnumber)-1-i]='6'

        if newlist==newnumber:
            return False
        else:
            return True
