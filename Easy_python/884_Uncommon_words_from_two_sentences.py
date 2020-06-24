class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        Ap=A.split()
        Bp=B.split()
        returnlist=[]
        newA=Counter(Ap)
        newB=Counter(Bp)
        for i in newA:
            if newA[i]==1:
                if i not in newB:
                    returnlist.append(i)
        for i in newB:
            if newB[i]==1:
                if i not in newA:
                    returnlist.append(i)
        return returnlist

