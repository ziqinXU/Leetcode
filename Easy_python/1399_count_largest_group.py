class Solution:
    def countLargestGroup(self, n: int) -> int:
        dictgroup={}
        i=1
        maxcount=0
        while i<=n:
            nsum=0
            templist=list(str(i))
            for j in range(len(templist)):
                nsum=nsum+int(templist[j])
            if nsum in dictgroup:
                dictgroup[nsum]=dictgroup[nsum]+1
            else:
                dictgroup[nsum]=1
            if nsum in dictgroup and dictgroup[nsum]>maxcount:
                maxcount=dictgroup[nsum]
            i=i+1
        total=0
        for i in dictgroup:
            if dictgroup[i]==maxcount:
                total=total+1
        return total
