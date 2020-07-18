class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dictint={}
        for i in range(lo,hi+1):
            number=i
            count=0
            while i!=1:
                if i%2==0:
                    i=i/2
                else:
                    i=3*i+1
                count=count+1
            dictint[number]=count
        A=sorted(dictint.items(),key = lambda x: (x[1],x[0]))#先按value排序，再按key
        return A[k-1][0]
